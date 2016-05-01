#coding:utf-8

from bs4 import BeautifulSoup
import os
import sys
import string
import codecs
from urllib import urlencode, quote
import requests
import re
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()

class pretreatment(object):
    def __init__(self):
        pass
    def read_txt(self, txtPath, coding = 'utf-8'):
        import codecs
        f = codecs.open(txtPath,'r',coding).readlines()
        f[0] = f[0].replace(u"\ufeff",u"")
        dataset = []
        for line in f:
            line = line.replace("\r\n","")
            line = line.replace("\n","")
            dataset.append(line)
        return dataset

    def writeMatrix(self, dataset, Path, coding = "utf-8"):
        for i in xrange(len(dataset)):
            temp = dataset[i]
            temp = [str(temp[j]) for j in xrange(len(temp))]
            temp = ",".join(temp)
            dataset[i] = temp
        string = "\n".join(dataset)
        f = open(Path, "a+")
        line = f.write(string+"\n")
        f.close()

class GenerateURL(object):
	def __init__(self):
		pass
	def generateFirstUrl(self, keyword, pageNum = 10):
		urlList = []
		keyword_encode = quote(keyword)
		url = 'http://news.baidu.com/ns?word='+keyword_encode
		url += '&pn=20&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0&rsv_page='
		for i in range(0, pageNum):
			urlList.append(url+str(i+1))
		return urlList

	def generateSecondUrl(self, keyword, pageNum = 10):
		urlList = self.generateFirstUrl(keyword, pageNum)
		secondUrlList = self.fliterUrl(urlList[0])
		print secondUrlList

	def fliterUrl(self, url):
		urlList = []
		r = requests.get(url)
		pattern = re.compile(r'<a href="(.*?)".*?', re.S)
		items = re.findall(pattern, r.content)
		urlList = [items[i] for i in xrange(len(items)) if 'http:' in items[i]]
		return urlList


class SinaGenerateURL(GenerateURL):
	def __init__(self):
		pass

	def fliterUrl(self, url):
		r = requests.get(url)
		pattern = re.compile(r'<a href="(.*?)".*?', re.S)
		items = re.findall(pattern, r.content)
		print items
		print items[-1]
		urlList = [items[i] for i in xrange(len(items)) if u'http://sports.sina.com' in items[i]]
		#print urlList[-1]
		return urlList


def main():
	keywords = pretreatment().read_txt('keywords.txt')
	keywords = [keyword.decode('utf-8').encode('gb2312') for keyword in keywords]
	#print keywords
	url = SinaGenerateURL().generateSecondUrl(keywords[0])
	print url




if __name__ == '__main__':
	main()