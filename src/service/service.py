import sys
import json
sys.path.append("..")
sys.path.append("../stanford-parser-python-r22186/src")
from image_processing.image_database import *
from stanford_parser.main import *
# import SocketServer
from flask import *
from flask_cors import CORS
# from flask_session import Session
app = Flask(__name__)
CORS(app)

#app.config['SESSION_TYPE'] = 'redis'
#Session(app)

#sess = Session()
#sess.init_app(app)


# class MyTCPHandler(SocketServer.BaseRequestHandler):
    # """
    # The RequestHandler class for our server.
    #
    # It is instantiated once per connection to the server, and must
    # override the handle() method to implement communication to the
    # client.
    # """

    # def handle(self):
    #     # self.request is the TCP socket connected to the client
    #     self.data = self.request.recv(1024).strip()
    #
    #     # keywords = parse(self.data)
    #     # image = getImage(keywords)
    #     print(self.data)
    #     # send back the data
    #     self.request.sendall(self.data)

# if __name__ == "__main__":
    # HOST, PORT = "129.31.171.191", 9999
    #
    # # Create the server, binding to localhost on port 9999
    # server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    #
    # # Activate the server; this will keep running until you
    # # interrupt the program with Ctrl-C
    # server.serve_forever()

# used to store previous images
#cache = {}

#app.secret_key = 'automatedstory'

def getCache():
    #cache = getattr(g, '_cache', None)
    #if cache is None:
    #    g._cache = {}
    
    #if 'cache' in session:
    #    return session['cache']
    
    return session.get('cache', {})

@app.route("/", methods = ['POST'])
def handle():
    # self.request is the TCP socket connected to the client
    # self.data = self.request.recv(1024).strip()
    #cache = getCache()
    #global cache
    data = request.form
    keywords = parse(str(data['text']))
    newScene = str(data['new_scene'])
    cache = json.loads(data['cache'])
    objects = []
    sys.stderr.write(str(keywords))

    temp = {'it':[], 'its':[], 'he':[], 'him':[], 'his':[], 'she':[], 'her':[], 'they':[], 'them':[], 'their':[], 'this':[], 'that':[], 'these':[], 'those':[]}
    for kw in keywords:
        img = []
        if kw['name']+str(kw['tags']) in cache: # image in cache
            img = cache[kw['name']+str(kw['tags'])]
        elif kw['name'] in cache:
            img = cache[kw['name']]
        elif kw['name'] not in temp: # the object is not 'he/she/it/they'
            img = getImage(kw) # get the image from database
            if img:
                cache[kw['name']+str(kw['tags'])] = img
                cache[kw['name']+str([])] = img

        person = ['it', 'its']
        # track 'he/she/it/they' in the sentence
        if 'male' in kw['tags'] or kw['name'] in ['he', 'him', 'his']:
            person = ['he', 'him', 'his']
        elif 'female' in kw['tags'] or kw['name'] in ['she', 'her']:
            person = ['she', 'her']
        elif kw['number'] > 1 or kw['name'] in ['they', 'them', 'their']:
            person = ['they', 'them', 'their']
        # replace the person if it's new or the sentence contains 'he/she/it/they'
        if not temp[person[0]] or kw['name'] in person:
            for p in person:
                temp[p] = img

        objects.append({
            "image": img,
            "size": kw['size'],
            "location": kw['location'],
            "speech": kw['speech']
        })

    for key in temp:
        if temp[key]:
            cache[key] = temp[key]
    objects.append({'cache': json.dumps(cache)})
    # setattr(g, '_cache', cache)
    #session['cache'] = cache
    
    # print log
    sys.stderr.write('cache = [')
    for key in cache:
        sys.stderr.write(key + ' ')
    sys.stderr.write(']')

    # image = getImage({
    #     'name': keywords['subject'],
    #     'tag': []
    # })
    # send back the data

    return jsonify(objects)
