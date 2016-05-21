# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask, send_from_directory, session, url_for, jsonify, abort, render_template
import os
import sys
import random
import datetime
import pymongo
from pymongo import MongoClient
import time
import spider
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.news

Title_Cut = 10
Content_Cut = 25
COUNT = 200

def create_app():
    _app = Flask(__name__)

    @_app.route('/')
    def homepage():
        #count = db.news.find().count()
        count = COUNT
        find = db.news.find()
        allNews = []
        for i in range(count):
            oneNews = {}
            oneNews['player'] = find[i]['player']
            if len(find[i]['title']) > 2*Title_Cut:
                oneNews['title1'] = find[i]['title'][0:Title_Cut]
                oneNews['title2'] = find[i]['title'][Title_Cut:2*Title_Cut]
            elif len(find[i]['title']) > Title_Cut:
                oneNews['title1'] = find[i]['title'][0:Title_Cut]
                oneNews['title2'] = find[i]['title'][Title_Cut:]
            else:
                oneNews['title1'] = find[i]['title'][0:]
                oneNews['title2'] = ''
            if len(find[i]['content']) > 2*Content_Cut:
                oneNews['content1'] = find[i]['content'][0:Content_Cut]
                oneNews['content2'] = find[i]['content'][Content_Cut:2*Content_Cut]
            elif len(find[i]['content']) > Title_Cut:
                oneNews['content1'] = find[i]['content'][0:Title_Cut]
                oneNews['content2'] = find[i]['content'][Title_Cut:]
            else:
                oneNews['content1'] = find[i]['content'][0:]
                oneNews['content2'] = ''
            oneNews['link'] = find[i]['link']
            oneNews['orgain'] = find[i]['orgain']
            oneNews['news_time'] = find[i]['news_time']
            allNews.append(oneNews)
        #print len(allNews)
        tips = {'p1':u'全部新闻','p2':u'全部队伍','p3':u'最多显示'+str(COUNT)+u'条新闻哦O(∩_∩)O~~'}
        return render_template('index.html',allNews=allNews,tips=tips)

    @_app.route('/soccer/mcf')
    def mcf():
        #count = db.news.find().count()
        find = db.news.find({'sports':u'足球','team':u'皇马'})
        count = min(find.count(), COUNT)
        allNews = []
        for i in range(count):
            oneNews = {}
            oneNews['player'] = find[i]['player']
            if len(find[i]['title']) > 2*Title_Cut:
                oneNews['title1'] = find[i]['title'][0:Title_Cut]
                oneNews['title2'] = find[i]['title'][Title_Cut:2*Title_Cut]
            elif len(find[i]['title']) > Title_Cut:
                oneNews['title1'] = find[i]['title'][0:Title_Cut]
                oneNews['title2'] = find[i]['title'][Title_Cut:]
            else:
                oneNews['title1'] = find[i]['title'][0:]
                oneNews['title2'] = ''
            if len(find[i]['content']) > 2*Content_Cut:
                oneNews['content1'] = find[i]['content'][0:Content_Cut]
                oneNews['content2'] = find[i]['content'][Content_Cut:2*Content_Cut]
            elif len(find[i]['content']) > Title_Cut:
                oneNews['content1'] = find[i]['content'][0:Title_Cut]
                oneNews['content2'] = find[i]['content'][Title_Cut:]
            else:
                oneNews['content1'] = find[i]['content'][0:]
                oneNews['content2'] = ''
            oneNews['link'] = find[i]['link']
            oneNews['orgain'] = find[i]['orgain']
            oneNews['news_time'] = find[i]['news_time']
            allNews.append(oneNews)
        tips = {'p1':u'足球新闻','p2':u'皇马','p3':u'最多显示'+str(COUNT)+u'条新闻哦O(∩_∩)O~~'}
        return render_template('index.html',allNews=allNews,tips=tips)

    @_app.route('/soccer/manutd')
    def manutd():
        #count = db.news.find().count()
        find = db.news.find({'sports':u'足球','team':u'曼联'})
        count = min(find.count(), COUNT)
        allNews = []
        for i in range(count):
            oneNews = {}
            oneNews['player'] = find[i]['player']
            if len(find[i]['title']) > 2*Title_Cut:
                oneNews['title1'] = find[i]['title'][0:Title_Cut]
                oneNews['title2'] = find[i]['title'][Title_Cut:2*Title_Cut]
            elif len(find[i]['title']) > Title_Cut:
                oneNews['title1'] = find[i]['title'][0:Title_Cut]
                oneNews['title2'] = find[i]['title'][Title_Cut:]
            else:
                oneNews['title1'] = find[i]['title'][0:]
                oneNews['title2'] = ''
            if len(find[i]['content']) > 2*Content_Cut:
                oneNews['content1'] = find[i]['content'][0:Content_Cut]
                oneNews['content2'] = find[i]['content'][Content_Cut:2*Content_Cut]
            elif len(find[i]['content']) > Title_Cut:
                oneNews['content1'] = find[i]['content'][0:Title_Cut]
                oneNews['content2'] = find[i]['content'][Title_Cut:]
            else:
                oneNews['content1'] = find[i]['content'][0:]
                oneNews['content2'] = ''
            oneNews['link'] = find[i]['link']
            oneNews['orgain'] = find[i]['orgain']
            oneNews['news_time'] = find[i]['news_time']
            allNews.append(oneNews)
        tips = {'p1':u'足球新闻','p2':u'曼联','p3':u'最多显示'+str(COUNT)+u'条新闻哦O(∩_∩)O~~'}
        return render_template('index.html',allNews=allNews,tips=tips)


    @_app.route('/soccer/bar')
    def bar():
        #count = db.news.find().count()
        find = db.news.find({'sports':u'足球','team':u'巴萨'})
        count = min(find.count(), COUNT)
        allNews = []
        for i in range(count):
            oneNews = {}
            oneNews['player'] = find[i]['player']
            if len(find[i]['title']) > 2*Title_Cut:
                oneNews['title1'] = find[i]['title'][0:Title_Cut]
                oneNews['title2'] = find[i]['title'][Title_Cut:2*Title_Cut]
            elif len(find[i]['title']) > Title_Cut:
                oneNews['title1'] = find[i]['title'][0:Title_Cut]
                oneNews['title2'] = find[i]['title'][Title_Cut:]
            else:
                oneNews['title1'] = find[i]['title'][0:]
                oneNews['title2'] = ''
            if len(find[i]['content']) > 2*Content_Cut:
                oneNews['content1'] = find[i]['content'][0:Content_Cut]
                oneNews['content2'] = find[i]['content'][Content_Cut:2*Content_Cut]
            elif len(find[i]['content']) > Title_Cut:
                oneNews['content1'] = find[i]['content'][0:Title_Cut]
                oneNews['content2'] = find[i]['content'][Title_Cut:]
            else:
                oneNews['content1'] = find[i]['content'][0:]
                oneNews['content2'] = ''
            oneNews['link'] = find[i]['link']
            oneNews['orgain'] = find[i]['orgain']
            oneNews['news_time'] = find[i]['news_time']
            allNews.append(oneNews)
        tips = {'p1':u'足球新闻','p2':u'巴萨','p3':u'最多显示'+str(COUNT)+u'条新闻哦O(∩_∩)O~~'}
        return render_template('index.html',allNews=allNews,tips=tips)

    @_app.route('/basketball/hr')
    def hr():
        #count = db.news.find().count()
        find = db.news.find({'sports':u'篮球','team':u'休斯顿火箭队'})
        count = min(find.count(), COUNT)
        allNews = []
        for i in range(count):
            oneNews = {}
            oneNews['player'] = find[i]['player']
            if len(find[i]['title']) > 2*Title_Cut:
                oneNews['title1'] = find[i]['title'][0:Title_Cut]
                oneNews['title2'] = find[i]['title'][Title_Cut:2*Title_Cut]
            elif len(find[i]['title']) > Title_Cut:
                oneNews['title1'] = find[i]['title'][0:Title_Cut]
                oneNews['title2'] = find[i]['title'][Title_Cut:]
            else:
                oneNews['title1'] = find[i]['title'][0:]
                oneNews['title2'] = ''
            if len(find[i]['content']) > 2*Content_Cut:
                oneNews['content1'] = find[i]['content'][0:Content_Cut]
                oneNews['content2'] = find[i]['content'][Content_Cut:2*Content_Cut]
            elif len(find[i]['content']) > Title_Cut:
                oneNews['content1'] = find[i]['content'][0:Title_Cut]
                oneNews['content2'] = find[i]['content'][Title_Cut:]
            else:
                oneNews['content1'] = find[i]['content'][0:]
                oneNews['content2'] = ''
            oneNews['link'] = find[i]['link']
            oneNews['orgain'] = find[i]['orgain']
            oneNews['news_time'] = find[i]['news_time']
            allNews.append(oneNews)
        tips = {'p1':u'篮球新闻','p2':u'休斯顿火箭队','p3':u'最多显示'+str(COUNT)+u'条新闻哦O(∩_∩)O~~'}
        return render_template('index.html',allNews=allNews,tips=tips)

    @_app.route('/basketball/lal')
    def lal():
        #count = db.news.find().count()
        find = db.news.find({'sports':u'篮球','team':u'湖人队'})
        count = min(find.count(), COUNT)
        allNews = []
        for i in range(count):
            oneNews = {}
            oneNews['player'] = find[i]['player']
            if len(find[i]['title']) > 2*Title_Cut:
                oneNews['title1'] = find[i]['title'][0:Title_Cut]
                oneNews['title2'] = find[i]['title'][Title_Cut:2*Title_Cut]
            elif len(find[i]['title']) > Title_Cut:
                oneNews['title1'] = find[i]['title'][0:Title_Cut]
                oneNews['title2'] = find[i]['title'][Title_Cut:]
            else:
                oneNews['title1'] = find[i]['title'][0:]
                oneNews['title2'] = ''
            if len(find[i]['content']) > 2*Content_Cut:
                oneNews['content1'] = find[i]['content'][0:Content_Cut]
                oneNews['content2'] = find[i]['content'][Content_Cut:2*Content_Cut]
            elif len(find[i]['content']) > Title_Cut:
                oneNews['content1'] = find[i]['content'][0:Title_Cut]
                oneNews['content2'] = find[i]['content'][Title_Cut:]
            else:
                oneNews['content1'] = find[i]['content'][0:]
                oneNews['content2'] = ''
            oneNews['link'] = find[i]['link']
            oneNews['orgain'] = find[i]['orgain']
            oneNews['news_time'] = find[i]['news_time']
            allNews.append(oneNews)
        tips = {'p1':u'篮球新闻','p2':u'湖人队','p3':u'最多显示'+str(COUNT)+u'条新闻哦O(∩_∩)O~~'}
        return render_template('index.html',allNews=allNews,tips=tips)

    @_app.route('/basketball/cb')
    def cb():
        #count = db.news.find().count()
        find = db.news.find({'sports':u'篮球','team':u'芝加哥公牛队'})
        count = min(find.count(), COUNT)
        allNews = []
        for i in range(count):
            oneNews = {}
            oneNews['player'] = find[i]['player']
            if len(find[i]['title']) > 2*Title_Cut:
                oneNews['title1'] = find[i]['title'][0:Title_Cut]
                oneNews['title2'] = find[i]['title'][Title_Cut:2*Title_Cut]
            elif len(find[i]['title']) > Title_Cut:
                oneNews['title1'] = find[i]['title'][0:Title_Cut]
                oneNews['title2'] = find[i]['title'][Title_Cut:]
            else:
                oneNews['title1'] = find[i]['title'][0:]
                oneNews['title2'] = ''
            if len(find[i]['content']) > 2*Content_Cut:
                oneNews['content1'] = find[i]['content'][0:Content_Cut]
                oneNews['content2'] = find[i]['content'][Content_Cut:2*Content_Cut]
            elif len(find[i]['content']) > Title_Cut:
                oneNews['content1'] = find[i]['content'][0:Title_Cut]
                oneNews['content2'] = find[i]['content'][Title_Cut:]
            else:
                oneNews['content1'] = find[i]['content'][0:]
                oneNews['content2'] = ''
            oneNews['link'] = find[i]['link']
            oneNews['orgain'] = find[i]['orgain']
            oneNews['news_time'] = find[i]['news_time']
            allNews.append(oneNews)
        tips = {'p1':u'篮球新闻','p2':u'芝加哥公牛队','p3':u'最多显示'+str(COUNT)+u'条新闻哦O(∩_∩)O~~'}
        return render_template('index.html',allNews=allNews,tips=tips)

    @_app.route('/today')
    def todaySpider():
        spider.spider()
        find = db.news.find({"insert_time":"2016-05-21"})
        count = min(find.count(), COUNT)
        allNews = []
        for i in range(count):
            oneNews = {}
            oneNews['player'] = find[i]['player']
            if len(find[i]['title']) > 2*Title_Cut:
                oneNews['title1'] = find[i]['title'][0:Title_Cut]
                oneNews['title2'] = find[i]['title'][Title_Cut:2*Title_Cut]
            elif len(find[i]['title']) > Title_Cut:
                oneNews['title1'] = find[i]['title'][0:Title_Cut]
                oneNews['title2'] = find[i]['title'][Title_Cut:]
            else:
                oneNews['title1'] = find[i]['title'][0:]
                oneNews['title2'] = ''
            if len(find[i]['content']) > 2*Content_Cut:
                oneNews['content1'] = find[i]['content'][0:Content_Cut]
                oneNews['content2'] = find[i]['content'][Content_Cut:2*Content_Cut]
            elif len(find[i]['content']) > Title_Cut:
                oneNews['content1'] = find[i]['content'][0:Title_Cut]
                oneNews['content2'] = find[i]['content'][Title_Cut:]
            else:
                oneNews['content1'] = find[i]['content'][0:]
                oneNews['content2'] = ''
            oneNews['link'] = find[i]['link']
            oneNews['orgain'] = find[i]['orgain']
            oneNews['news_time'] = find[i]['news_time']
            allNews.append(oneNews)
        tips = {'p1':u'今日爬取新闻','p2':u' ','p3':u'最多显示'+str(COUNT)+u'条新闻哦O(∩_∩)O~~'}
        return render_template('index.html',allNews=allNews,tips=tips)
    return _app

def configure_jinja2(app):
    app.jinja_env.trim_blocks = True

    @app.template_filter()
    def time_delta(d, **params):
        return d + datetime.timedelta(**params)

def configure_logging(app):
    """Configure file(info) and email(error) logging."""
    import logging
    from logging.handlers import RotatingFileHandler

    file_handler = RotatingFileHandler(os.path.join(app.config['LOG_PATH'], 'ingsoccer.log'), maxBytes=100000, backupCount=10)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('[%(asctime)s](%(levelname)s) %(message)s  [%(pathname)s:%(lineno)d]'))
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
