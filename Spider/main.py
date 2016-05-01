#coding:utf-8

from bs4 import BeautifulSoup
import os
import sys
import string
import codecs
from urllib import urlencode, quote
import requests
import re
import time
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
            temp = "*****".join(temp)
            dataset[i] = temp
        string = "\n".join(dataset)
        f = open(Path, "a+")
        line = f.write(string+"\n")
        f.close()

class GenerateURLSpider(object):
    def __init__(self):
        pass
    def generateFirstUrl(self, keyword, pageNum = 10):
        urlList = []
        #keyword_encode = quote(keyword)
        url = 'http://news.baidu.com/ns?word='+keyword
        url += '&pn=20&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0&rsv_page='
        for i in range(0, pageNum):
            urlList.append(url+str(i+1))
        return urlList

    def generateSecondUrl(self, keyword, pageNum = 10):
        urlList = self.generateFirstUrl(keyword, pageNum)
        secondUrlList = []
        for i in range(len(urlList)):
            secondUrlList.extend(self.fliterUrl(urlList[i]))
        #print secondUrlList,len(secondUrlList)
        return secondUrlList

    def fliterUrl(self, url):
        urlList = []
        r = requests.get(url)
        pattern = re.compile(r'<a href="(.*?)".*?', re.S)
        items = re.findall(pattern, r.content)
        urlList = [items[i] for i in xrange(len(items)) if u'http:' in items[i]]
        return urlList

    def urlSpider(self, keyword):
        urlList = self.generateSecondUrl(keyword)
        content = [[]]
        return content

    def contentSpider(self, url):
        pass

    def dropHtmlTag(self, htmlStr):
        self.htmlStr = htmlStr
        re_cdata=re.compile('//]*//\]\]>',re.I)
        re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)
        re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)
        re_br=re.compile('')
        re_h=re.compile(']*>')
        re_comment=re.compile('')
        s=re_cdata.sub('',htmlStr)
        s=re_script.sub('',s)
        s=re_style.sub('',s)
        s=re_br.sub('\n',s)
        blank_line=re.compile('\n+')
        s = blank_line.sub('\n',s)
        s=re_h.sub('',s)
        s=re_comment.sub('',s)
        blank_line=re.compile('\n+')
        s=blank_line.sub('\n',s)
        return s

class SinaGenerateURLSpider(GenerateURLSpider):
    def __init__(self):
        pass

    def fliterUrl(self, url):
        #print url
        r = requests.get(url)
        pattern = re.compile(r'<a href="(.*?)".*?', re.S)
        items = re.findall(pattern, r.content)
        urlList = [items[i] for i in xrange(len(items)) if u'http://sports.sina.com' in items[i]]
        return urlList

    def urlSpider(self, keyword):
        result = []
        urlList = self.generateSecondUrl(keyword)
        #content = self.contentSpider(urlList[0])
        if len(urlList) != 0:
            for i in range(len(urlList)):
                content = self.contentSpider(urlList[i])
                time.sleep(3)
                result.append(content)
        return result

    def contentSpider(self, url):
        r = requests.get(url)
        #print r.content
        if r.encoding != 'utf-8':r.encoding='utf-8'
        soup = BeautifulSoup(r.content)
        title = soup.title.string
        try:
            date = soup.find(id="pub_date")
            date = date.string
        except:
            date ='none'

        content = soup.find(id="artibody")
        content = content.find_all('p')
        try:
            content = [content[i].string.strip() for i in range(len(content))]
            content = ''.join(content)
        except:
            content = title
        # print content
        return [title, date, content]

class netEaseGenerateURLSpider(GenerateURLSpider):
    def __init__(self):
        pass

    def fliterUrl(self, url):
        #print url
        r = requests.get(url)
        pattern = re.compile(r'<a href="(.*?)".*?', re.S)
        items = re.findall(pattern, r.content)
        urlList = [items[i] for i in xrange(len(items)) if u'http://news.163.com' in items[i]]
        return urlList

    def urlSpider(self, keyword):
        result = []
        urlList = self.generateSecondUrl(keyword)
        #content = self.contentSpider(urlList[0])
        if len(urlList) != 0:
            for i in range(len(urlList)):
                content = self.contentSpider(urlList[i])
                time.sleep(3)
                result.append(content)
        return result

    def contentSpider(self, url):
        r = requests.get(url)
        #print r.content
        if r.encoding != 'utf-8':r.encoding='utf-8'
        soup = BeautifulSoup(r.content)
        title = soup.title.string
        try:
            date = soup.find(attrs={'class':'ep-time-soure cDGray'})
            date = date.string
        except:
            date = 'none'
        content = soup.find(id="endText")
        content = content.find_all('p')
        try:
            content = [content[i].string.strip() for i in range(len(content))]
            content = ''.join(content)
        except:
            content = title
        # print content
        return [title, date, content]

def main():
    keywords = pretreatment().read_txt('keywords.txt')
    #keywords = [keyword.decode('utf-8').encode('gb2312') for keyword in keywords]
    #print keywords
    for ii in range(len(keywords)):
        result = SinaGenerateURLSpider().urlSpider(keywords[ii])
        for i in range(len(result)):
            temp = result[i]
            temp.append(keywords[ii])
            result[i] =temp
        pretreatment().writeMatrix(result,'result.txt')

def netEaseMain():
    keywords = pretreatment().read_txt('keywords.txt')
    for ii in range(len(keywords)):
        result = netEaseGenerateURLSpider().urlSpider(keywords[ii])
        for i in range(len(result)):
            temp = result[i]
            temp.append(keywords[ii])
            result[i] =temp
        pretreatment().writeMatrix(result,'result.txt')

if __name__ == '__main__':
    main()
    netEaseMain()