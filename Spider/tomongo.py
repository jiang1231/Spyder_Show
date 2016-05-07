#conding:utf-8
from handle import dataset
import pymongo
from pymongo import MongoClient
import time
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.news

#title,link,orgain,content,keywords
def insert():
	result = dataset()
	print len(result),result[0][0]
	nowtime = str(time.strftime("%Y-%m-%d", time.localtime()))
	#print nowtime,type(nowtime)
	#db.news.find_one({'link'})
	[player,team,sports] = result[0][4].split()
	[orgain,news_time] = result[0][2].split('&nbsp;&nbsp;')
	print orgain,news_time
	#print player,'ss',team,'ss',sports
	post = {'insert_time':nowtime,'title':result[0][0],'link':result[0][1],'orgain':orgain,'news_time':news_time,'content':result[0][3],'player':player,'team':team,'sports':sports}
	print post
	#db.news.insert_one(post)
	find = db.news.find_one({'link':result[0]})
	print str(find)
	if str(find) == 'None':
		print 'hh'

	for i in range(len(result)):
		temp = result[i]
		find = db.news.find_one({'link':temp[1]})
		if str(find) == 'None':
			[player,team,sports] = temp[4].split()
			try:
				[orgain,news_time] = temp[2].split('&nbsp;&nbsp;')
			except:
				orgain = temp[2]
				news_time = temp[2]
			nowtime = str(time.strftime("%Y-%m-%d", time.localtime()))
			post = {'insert_time':nowtime,'title':temp[0],'link':temp[1],'orgain':orgain,'news_time':news_time,'content':temp[3],'player':player,'team':team,'sports':sports}
			db.news.insert_one(post)
	print 'finished'


if __name__ == '__main__':
	count = db.news.find().count()
	find = db.news.find()
	allNews = []
	print find[0],type(find[0])
	for i in range(count):
		allNews.append(find[i])
	print len(allNews)




