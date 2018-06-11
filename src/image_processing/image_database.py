import os
import random
import MySQLdb
import PIL.Image as Image
import numpy as np
import base64
import extract_color
import dynamic_crawler
import sys

# DEFINED COLOR NAME
color = ['cyan','red', 'pink', 'orange', 'blue', 'yellow', 'green', 'purple', 'brown', 'grey', 'white', 'black']

# GET IMAGE NAME IN IMAGE_LIBRARY FOLDER
# namelist = []
# path = "../image_processing/image_library"
# for name in os.listdir(path):
#     namelist.append(name)

# DISJUDGE WHETHER TAGS ONLY CONTAIN COLOR ATTRIBUTES
def onlyColorInTags(object):
    if(len(object['tags'])==0):
        return 0
    else:
        for element in object['tags']:
            if(element not in color):
                return 0
        return 1

# GET COLOR NAME FROM TAGS
def getColorInTags(tags):
    for ele in tags:
        if ele in color:
            return ele
    return 'None'

# DISJUDGE WHETHER THE OBJECT'S NAME IN DATABASE
def nameIndb(object):
    try:
        object['name']
    except Exception as e:
      return 0
    db = MySQLdb.connect("localhost","root","zhanghan","IMAGE_DB")
    cursor = db.cursor()
    look_up = "SELECT * FROM IMAGE WHERE name = '%s'" % (object['name'])
    cursor.execute(look_up)
    results = cursor.fetchall()
    cursor.close()
    db.close()
    if not results:
        return 0
    # for name in namelist:
    #     if(object['name'] == name):
    #         return 1
    return 1

# GET NEW TAGS FORM THE OBJECT
def getNewTag(object):
    new_tag = []
    flag = False
    for ele in object['tags']:
        if ele != 'properNoun' and ele != 'personName':
            new_tag.append(ele)
        else:
            flag = True
    if(flag == False):
        new_tag.append(object['name'])
    return new_tag

# MAIN FUNCTION TO GET IMAGE FORM OBJECT PARAMETER
def getImage(object):
    ls_f = []
    dynamic_ls_f = []
    if object['number'] and object['name']:
        try:
            db = MySQLdb.connect("localhost","hm1416","","prj")
            db.autocommit(True)
            cursor = db.cursor()
            # name corresponds to name in database, color corresponds to color attributes in database.
            # the object name exists in database
            if(nameIndb(object) == 1):
                if(len(object['tags']) == 0):
                    look_up = "SELECT * FROM IMAGE WHERE name = '%s'" % (object['name'])
                    for times in range(object['number']):
                        cursor.execute(look_up)
                        results = cursor.fetchall()
                        index = random.randint(0, len(results) - 1)
                        row  = results[index]
                        img_path = row[3]
                        f = open('../image_processing/' + img_path,'rb')
                        ls_f.append(base64.b64encode(f.read()))
                        f.close()
                elif(onlyColorInTags(object) == 1):
                    look_up = "SELECT * FROM IMAGE WHERE name = '%s' AND color = '%s'" % (object['name'], object['tags'][0])
                    cursor.execute(look_up)
                    results = cursor.fetchall()
                    if(not results):
                        new_tag = getNewTag(object)
                        new_color = getColorInTags(new_tag)
                        new_ls_f = dynamic_crawler.dynamic_crawler(new_tag)[0][0]
                        for i in range(0, object['number']):
                            dynamic_ls_f.append(new_ls_f)
                        name = dynamic_crawler.dynamic_crawler(new_tag)[1]
                        path = dynamic_crawler.dynamic_crawler(new_tag)[2]
                        sql = "INSERT INTO IMAGE(name, color, img_path) VALUES ('" + name + "', '" + new_color + "', '" + path + "')"
                        cursor.execute(sql)
                        return dynamic_ls_f
                    else:
                        for times in range(object['number']):
                            cursor.execute(look_up)
                            results = cursor.fetchall()
                            index = random.randint(0, len(results) - 1)
                            row  = results[index]
                            img_path = row[3]
                            f = open('../image_processing/' + img_path,'rb')
                            ls_f.append(base64.b64encode(f.read()))
                            f.close()

                else:
                    new_tag = getNewTag(object)
                    if(len(new_tag) == 0):
                        return dynamic_ls_f
                    new_color = getColorInTags(new_tag)
                    new_ls_f = dynamic_crawler.dynamic_crawler(new_tag)[0][0]
                    for i in range(0, object['number']):
                        dynamic_ls_f.append(new_ls_f)
                    name = dynamic_crawler.dynamic_crawler(new_tag)[1]
                    path = dynamic_crawler.dynamic_crawler(new_tag)[2]
                    sql = "INSERT INTO IMAGE(name, color, img_path) VALUES ('" + name + "', '" + new_color + "', '" + path + "')"
                    cursor.execute(sql)
                    return dynamic_ls_f

            # the object name does not exist in database
            else:
                new_tag = getNewTag(object)
                if(len(new_tag) == 0):
                    return dynamic_ls_f
                new_color = getColorInTags(new_tag)
                new_ls_f = dynamic_crawler.dynamic_crawler(new_tag)[0][0]
                for i in range(0, object['number']):
                    dynamic_ls_f.append(new_ls_f)
                name = dynamic_crawler.dynamic_crawler(new_tag)[1]
                path = dynamic_crawler.dynamic_crawler(new_tag)[2]
                sql = "INSERT INTO IMAGE(name, color, img_path) VALUES ('" + name + "', '" + new_color + "', '" + path + "')"
                cursor.execute(sql)
                return dynamic_ls_f
            # db.commit()
            cursor.close()
            db.close()
        except Exception as e:
           print("Error: unable to fetch data: " + str(e))
           sys.stderr.write("Error: unable to fetch data: " + str(e));

    return ls_f

# object = {'name': 'mushroom', 'tags': ['blue'], 'number': 1}
# getImage(object)

# if __name__ == '__main__':
#     object = {'name':'pigs', 'tags': [], 'number':5}
#     print len(getImage(object))

## HELPER FUNCTION TO DISJUDGE WHETHER ONE FILE IS IMAGE
# def isimage(fn):
#     return os.path.splitext(fn)[-1] in ('.jpg', '.JPG', '.png', '.PNG')

## HELPER FUNCTION TO GET ALL PATH AND TAGS OF IMAGES IN LIBRARY
# pathlist = []
# namelist = []
# colorlist = []
# for r, ds, fs in os.walk("./image_library"):
#     for filename in fs:
#         fullpath = os.path.join(r, filename)
#         if isimage(filename):
#             name_in_db = r[16:]
#             namelist.append(name_in_db)
#             pathlist.append(fullpath)
#             colorlist.append(extract_color.get_color_name(Image.open(fullpath)))
# print namelist

## CONNECT TO MYSQL DATABASE
# db = MySQLdb.connect("localhost","root","zhanghan","IMAGE_DB")
# cursor = db.cursor()
## SAVE IMAGES IN IMAGE_LIBRARY INTO IMAGEDATABASE
# try:
#     for img_id in range(0,len(namelist)):
#         cursor.execute("INSERT INTO IMAGE(id, name, color, img_path) \
#                         VALUES ('%d', '%s', '%s', '%s')" % \
#                         (img_id, namelist[img_id], colorlist[img_id], pathlist[img_id]))
#         db.commit()
#
# except:
#    db.rollback()

#db.close()
