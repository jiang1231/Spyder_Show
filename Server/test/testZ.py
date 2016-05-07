# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import random
import datetime
import pymongo
from pymongo import MongoClient
import time
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.news


find = db.news.find({'sports':u'篮球','team':u'达斯拉小牛队'})
print find.count()