#! python

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

URL = 'http://www.pythonscraping.com/pages/warandpeace.html'
URL1 = 'http://www.pythonscraping.com/pages/page3.html'


def getName():
    html = urlopen(URL)
    bsObj = BeautifulSoup(html)
    nameList = bsObj.findAll("span", {"class": "green"})
    for name in nameList:
        print(name)
        # 清除所有的标签，返回文字内容
        print(name.get_text())


def getChild():
    html = urlopen(URL1)
    bsObj = BeautifulSoup(html)
    # for child in bsObj.find("table", {"id":"giftList"}).children:
    # print(child)

    # for silbing in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
    #     print(silbing)


def getImage():
    html = urlopen(URL1)
    bsObj = BeautifulSoup(html)
    images = bsObj.findAll('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})
    for image in images:
        print(image['src'])

def getTagByLambda():
    html = urlopen(URL1)
    bsObj = BeautifulSoup(html)
    tags = bsObj.findAll(lambda tag:len(tag.attrs)==2)
    for tag in tags:
        print(tag)


if __name__ == '__main__':
    # getName()
    # getChild()
    # getImage()
    getTagByLambda()
