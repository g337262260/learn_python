#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""xml-html"""

__author__ = 'Guowei'

from xml.parsers.expat import ParserCreate
from urllib import request
from html.parser import HTMLParser
from html.entities import name2codepoint
import re
import requests
from lxml import html
#-------------------------------------------------------------------------------------
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
# 随机字母
def rndChar():
    return chr(random.randint(65,90))
# 随机颜色
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
# 随机颜色2
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

def getImage():
    width = 60*4
    height = 60
    image = Image.new('RGB',(width,height),(255,255,255))
    # 创建Font对象
    font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf',36)
    # 创建draw对象
    draw = ImageDraw.Draw(image)
    # 填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rndColor())
    # 输出文字
    for t in range(4):
        draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())

    # 模糊
    image = image.filter(ImageFilter.BLUR)
    image.save(r'C:\Users\Administrator\Desktop\char.jpg','jpeg')
    image.show()
    print('Complete')







#---------------------------------------------------------------------------

def fetchWebData(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)
    # print(tree)
    titles=tree.xpath('//h3[@class="event-title"]/a/text()')
    times=tree.xpath('//h3/../p/time/@datetime')
    locations=tree.xpath('//span[@class="event-location"]/text()')
    processdata=map(lambda x,y,z:{'event-title':x,'event-time':y,'event-location':z} ,titles,times,locations)
    for n in processdata:
        print (n)
class MyHTMLParser(HTMLParser):

    # 初始化操作
    def __init__(self):
        HTMLParser.__init__(self)
        self.isTime = False
        self.isTitle = False
        self.isLocation = False
        self.isYear = False
        self.item = {}
        self.metting = []
    # 在开始标签处 打开标记 收集数据
    def handle_starttag(self, tag, attrs):
        if tag =='time':
            self.isTime = True
        if ('class','event-title') in attrs:
            self.isTitle = True
        if ('class','event-location') in attrs:
            self.isLocation = True
        if ('class', 'say-no-more') in attrs:
            self.isYear = True
    # 在结束标签关闭标记 停止手机数据
    def handle_endtag(self, tag):
        if tag =='li' and len(self.item)>0:
            self.metting.append(self.item)
            self.item = {}
    # 收集数据
    def handle_data(self, data):
        if self.isTitle:
            self.item['Title'] = data
            self.isTitle = False
        if self.isTime:
            self.item['Time'] = data
            self.isTime = False
        if self.isYear:
            if re.match(r'\d{4}',data.strip()):
                self.item['Year'] = data
                self.isYear = False
        if self.isLocation:
            self.item['Location'] = data
            self.isLocation = False


    # def handle_startendtag(self, tag, attrs):
    #     print('3<%s/>' % tag)
    # def handle_comment(self, data):
    #     print('4<!--', data, '-->')
    #
    # def handle_entityref(self, name):
    #     print('5&%s;' % name)
    #
    # def handle_charref(self, name):
    #     print('6&#%s;' % name)
class DefaultSaxHandler(object):
    weather = {'city':'','forecast':[]}

    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.weather['city'] = attrs['city']
        if name == 'yweather:forecast':
            self.weather['forecast'].append({'date':attrs['date'],'high':attrs['high'],'low':attrs['low']})
def url_request(url):
    URL = 'https://www.python.org/events/python-events/'
    with request.urlopen(url) as weather:
        data = weather.read()
        handler = DefaultSaxHandler()
        parser = ParserCreate()
        parser.StartElementHandler = handler.start_element
        parser.Parse(url_request(URL))
        print(handler.weather)
if __name__ == '__main__':
    # URL = 'https://www.python.org/events/python-events/'
    #     # with request.urlopen(URL) as python_meeting:
    #     #     data = python_meeting.read()
    #     #     parser = MyHTMLParser()
    #     #     parser.feed(data.decode('utf-8'))
    #     # for i, event in enumerate(parser.metting):
    #     #     print(event)

    # fetchWebData('https://www.python.org/events/python-events/')
    getImage()