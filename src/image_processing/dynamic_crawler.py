import urllib2
import urllib
import re
import os
import requests
from bs4 import BeautifulSoup
import base64
import numpy as np
import sys

pre_url = 'https://www.google.co.uk/search?q=cartoon'

post_url = 'png&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwic5cP48Z3aAhUJL8AKHWtxACcQsAQIJw&biw=1440&bih=782'

hea = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}


def dynamic_crawler(tag, number = 1):

    if len(tag) == 0:
        return

    # when the tag is not null
    url = pre_url
    for element in tag:
        url = url + '+' + element
        name = element
    url = url + '+' + post_url
    html = requests.get(url,headers = hea)
    # resolve the html
    soup = BeautifulSoup(html.content, 'html.parser')
    new_set = soup.find_all(class_ = 'rg_meta notranslate', jsname = 'ik8THc')
    new_items = []
    ls_f = []

    # extract the images
    for element in new_set:
        pattern = re.compile('.*?"ou":"(.*?)".*?',re.S)
        items = re.findall(pattern, element.string)
        for ele in items:
            if ele.endswith('.png') and len(new_items) < max(number, 10):
                new_items.append(ele)

    # return the image list of corresponding length
    if len(new_items) > number:
        index = np.random.randint(len(new_items),size = number)
        for element in index:
            ele = new_items[element]
            u = urllib.urlopen(ele)
            data = u.read()
            path = './new_image/'+name+ '.png'
            f = open(path, 'wb')
            f.write(data)
            f.close()
            ls_f.append(base64.b64encode(data))
            path = 'new_image/'+name+ '.png'
        return ls_f, name, path

    else:
        for i in range(number):
            ele = new_items[i % len(new_items)]
            u = urllib.urlopen(ele)
            data = u.read()
            path = './new_image/'+name+ '.png'
            f = open(path, 'wb')
            f.write(data)
            f.close()
            ls_f.append(base64.b64encode(data))
            path = 'new_image/'+name+ '.png'
        return ls_f, name, path

if __name__ == '__main__':
    print dynamic_crawler(['green', 'apple'])[0]
