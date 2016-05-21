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
        # url += '&pn=0&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0'
        url += '&sr=0&cl=2&rn=20&tn=news&ct=0&clk=sortbytime'
        return url

    def contentSpider(self, content, keyword):
        link = content.find('a').get('href')
        # print link,type(link)
        find = db.news.find_one({'link':link})
        # find = 'None'
        if str(find) == 'None':
            try:
                title = content.a.get_text()
            except:
                title = ''
            # print title,type(title)
            try:
                detail = content.find('p',attrs={'class':'c-author'})
                # print detail.get_text()
                [orgain, news_time] = detail.get_text().split('***')
                # print orgain,news_time,type(orgain)
                content.find('p',attrs={'class':'c-author'}).string = ''
            except:
                orgain, news_time = '',''

            try:
                content.find('span',attrs={'class':'c-info'}).string = ''
                news = content.find('div',attrs={"class":'c-summary c-row '})
                news = news.get_text().strip()
            except:
                news = ''
            if news == '':
                try:
                    content.find('span',attrs={'class':'c-info'}).string = ''
                    news = content.find('div',attrs={'class':'c-span18 c-span-last'})
                    news = news.get_text().strip()
                except:
                    news =''
            # print news,'ss'

            nowtime = str(time.strftime("%Y-%m-%d", time.localtime()))
            [player,team,sports] = keyword.split()
            post = {'insert_time':nowtime,'link':link,'title':title,'orgain':orgain,'news_time':news_time,'content':news,'player':player,'team':team,'sports':sports}
            print post
            if news != '' and title != '':
                db.news.insert_one(post)
            #print news

    def urlSpider(self, keyword):
        url = self.generateUrl(keyword)
        r = requests.get(url)
        if r.encoding != 'utf-8':r.encoding='utf-8'
        html = r.content
        html.replace(u'&nbsp;&nbsp;','***')
        html = html.split('&nbsp;&nbsp;')
        html = '***'.join(html)
        soup = BeautifulSoup(html)
        contents = soup.find_all("div", attrs={"class": "result"})
        if len(contents) != 0:
            for i in range(len(contents)):
                self.contentSpider(contents[i], keyword)

def spider():
    for i in range(len(keywords)):
        keyword = keywords[i]
        SpiderKeywords().urlSpider(keyword)
        
if __name__ == '__main__':
    spider()