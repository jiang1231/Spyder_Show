#conding:utf-8
from flask import Flask, send_from_directory, session, url_for, jsonify, abort, render_template
import os
import sys
import random
import datetime
import pymongo
from pymongo import MongoClient
import time
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.news

Title_Cut = 7
Content_Cut = 14

def create_app():
    _app = Flask(__name__)

    @_app.route('/')
    def homepage():
        #count = db.news.find().count()
        count = 200
        find = db.news.find()
        allNews = []
        for i in range(count):
            oneNews = {}
            oneNews['player'] = find[i]['player']
            if len(find[i][title]) > 2*Title_Cut:
                oneNews['title1'] = find[i][title][0:Title_Cut]
                oneNews['title2'] = find[i][title][Title_Cut:2*Title_Cut]
            elif len(find[i][title]) > Title_Cut:
                oneNews['title1'] = find[i][title][0:Title_Cut]
                oneNews['title2'] = find[i][title][Title_Cut:]
            else:
                oneNews['title1'] = find[i][title][0:]
                oneNews['title2'] = ''
            
            allNews.append(find[i])
        #print len(allNews)
        return render_template('index.html',allNews=allNews)


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
