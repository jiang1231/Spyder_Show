import pymongo
from pymongo import MongoClient
import time
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.news

Title_Cut = 7
Content_Cut = 14

if __name__ == '__main__':
    count = 200
    find = db.news.find()
    allNews = []
    oneNews = {}
    for i in range(count):
    	#print find[i]
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
    print allNews[0],allNews[1],len(allNews)
    print allNews[0] == allNews[1]
