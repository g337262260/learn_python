#! python3
"""
    #: 测试连接mysql
    #: Guowei
"""

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, CHAR, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from requests_html import HTMLSession
import time
import re

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'
USERNAME = 'root'
PASSWORD = '123456'

DBURI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8". \
    format(username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE)

BaseModel = declarative_base()
engine = create_engine(DBURI)
Session = sessionmaker(bind=engine)
session = Session()

h_session = HTMLSession()

TYPE = 1
SORT = 8
"""
    # 1:分类
    # 2018：年份
    # 8：评分排序
    # 2：页数
    # 1：
"""
AIQIYI = 'https://list.iqiyi.com/www/{0}/-----------{1}--{2}-{3}-1-iqiyi--.html'


def initDb():
    BaseModel.metadata.create_all(engine)


def dropDb():
    BaseModel.metadata.drop_all()


def createTable():
    conn = engine.connect()
    result = conn.execute("select 1")
    print(result.fetchone())


class Movie(BaseModel):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True,unique=True)
    title = Column(String(255))
    category = Column(Integer)
    year = Column(Integer)
    duration = Column(String(30))
    url = Column(String(255))
    summary = Column(Text)
    image_url = Column(String(255))
    score = Column(Float)
    language = Column(String(30))
    role = Column(String(100))


def saveData(url,year):
    r = h_session.get(url)
    sel1 = 'body > div.page-list.page-list-type1 > div > div > div.wrapper-cols > div > ul > li > ' \
           'div.site-piclist_pic > a '
    sel_image = 'body > div.page-list.page-list-type1 > div > div > div.wrapper-cols > div > ul > li> ' \
                'div.site-piclist_pic > a > img '
    sel_rating = 'body > div.page-list.page-list-type1 > div > div > div.wrapper-cols > div > ul > li> ' \
                 'div.site-piclist_info > div.mod-listTitle_left '
    sel_role = 'body > div.page-list.page-list-type1 > div > div > div.wrapper-cols > div > ul > li > ' \
               'div.site-piclist_info '
    movie_list = []
    try:
        results = r.html.find(sel1)
        for result in results:
            movie = {'title': result.attrs['title'], 'duration': result.text, 'url': list(result.absolute_links)[0]}
            movie_list.append(movie)
    except:
        raise ValueError('title,duration,url')
    print("title,duration,url" + str(len(movie_list)))
    time.sleep(1)
    # ----------------------------------------------------------------------------------------------------------------
    try:
        results_image = r.html.find(sel_image)
        image_list = []
        for result in results_image:
            image_list.append(result.attrs['src'])
    except:
        raise ValueError('image')
    print("image" + str(len(image_list)))
    time.sleep(1)
    # ----------------------------------------------------------------------------------------------------------------
    try:
        results_score = r.html.find(sel_rating)
        score_list = []
        for result in results_score:
            score = result.text[:3]
            pattern = re.compile('[0-9]\.[0-9]')
            match = pattern.findall(score)
            if match:
                score_list.append(score)
            else:
                score_list.append("0")
    except:
        raise ValueError('score')
    print("score" + str(len(score_list)))
    time.sleep(1)
    # ----------------------------------------------------------------------------------------------------------------
    try:
        results_role = r.html.find(sel_role)
        role_list = []
        for result in results_role:
            if '主演' in result.text:
                index = result.text.index('主演')
                role_list.append(result.text[index:][:99])
            else:
                role_list.append('未知')
    except:
        raise ValueError('role')
    print("role" + str(len(role_list)))
    # ----------------------------------------------------------------------------------------------------------------
    for i, value in enumerate(movie_list):
        value['image_url'] = image_list[i]
        value['score'] = score_list[i]
        value['role'] = role_list[i]
    # ----------------------------------------------------------------------------------------------------------------
    for movie in movie_list:
        movie_item = Movie()
        movie_item.title = movie['title']
        movie_item.duration = movie['duration']
        movie_item.url = movie['url']
        movie_item.image_url = movie['image_url']
        movie_item.score = movie['score']
        movie_item.role = movie['role']
        movie_item.year = year
        movie_item.category = TYPE
        session.add(movie_item)
    session.commit()
    print('save database' + str(len(movie_list)))


def getData():
    try:
        #: 年份
        for y in range(2000,2019):
            # ：页数
            year = y
            for p in range(0,8):
                page = p
                url = AIQIYI .format(str(TYPE), str(year), str(SORT), str(page))
                print('url----'+url)
                saveData(url,year)
            print('Year: %s 结束了' % year)
    except:
        raise ValueError('Error----year：'+str(year)+'------page:'+str(page))


if __name__ == '__main__':
    # initDb()
    # saveData(AIQIYI)
    getData()
