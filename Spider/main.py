# -*- coding: utf-8 -*-
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()
from bs4 import BeautifulSoup
import string
import codecs
from urllib import urlencode, quote
import requests
import re
import time
from keywords import keywords
from pymongo import MongoClient
import time
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.news


class SpiderKeywords(object):
    def __init__(self):
        pass
    def generateUrl(self, keyword):
        url = 'http://news.baidu.com/ns?word='+keyword
        url += '&pn=0&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0'
        return url

    def contentSpider(self, content):
    	#content = content.decode('gb2312')
    	# print content
        link = content.find('a').get('href')
        print link,type(link)
  #       find = db.news.find_one({'link':temp[1]})
        # if str(find) == 'None':

        title = content.a.get_text()
        print title,type(title)

        detail = content.find('p',attrs={'class':'c-author'})
        print detail.get_text()
        # [orgain, news_time] = detail.get_text().split('\xa0\xa0')
        # print orgain,news_time



        news = content.find('div',attrs={"class":'c-summary c-row '})
        print news.get_text()
        #news = str(news).split('&nbsp;&nbsp;')


        nowtime = str(time.strftime("%Y-%m-%d", time.localtime()))
        # post = {'insert_time':nowtime,'title':temp[0],'link':temp[1],'orgain':orgain,'news_time':news_time,'content':temp[3],'player':player,'team':team,'sports':sports}
        post = {'insert_time':nowtime,'link':link,'title':title,'detail':detail}
        print post
        #db.news.insert_one(post)
        #print news




    def urlSpider(self, keyword):
        url = self.generateUrl(keyword)
        r = requests.get(url)
        #print type(r.content)
        #html = r.content.replace('\xa0','')
        #print type(html)
        if r.encoding != 'utf-8':r.encoding='utf-8'

        html = r.content
        print type(html)
        if u'&nbsp;&nbsp;' in html:
        	print 'jjjjjjjjj'

        html.replace(u'&nbsp;&nbsp;','***')
        if u'&nbsp;&nbsp;' in html:
        	print 'jjjjjjjjj'
        html = html.split('&nbsp;&nbsp;')
        html = '***'.join(html)
        print len(html)
        if u'&nbsp;&nbsp;' in html:
        	print 'jjjjjjjjj'
        # r.content.replace('&nbsp;&nbsp;','')
        with open('a.txt','w') as file:
        	file.write(html)
        soup = BeautifulSoup(html)
        contents = soup.find_all("div", attrs={"class": "result"})
        print len(contents)
        # print contents[0],type(contents[0])
        self.contentSpider(contents[0])




def spider():
    for i in range(len(keywords)):
        keyword = keywords[i]
        SpiderKeywords().urlSpider(keyword)
        break


if __name__ == '__main__':
    spider()