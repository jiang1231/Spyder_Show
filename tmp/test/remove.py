# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import time
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.news

find = db.news.find()
count = db.news.find().count()
time_remove = []
for i in range(count):
	try:
		time_ = find[i]['news_time']
		if u'2013年' in time_ or u'2014年' in time_:
			db.news.remove({'_id':find[i]['_id']})
		if u'小时' in time_ or u'分钟' in time_:
			db.news.update({"_id":find[i]["_id"]},{"$set":{"news_time":find[i]['insert_time']}})
	except:
		db.news.remove({'_id':find[i]['_id']})




