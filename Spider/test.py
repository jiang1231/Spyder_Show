#conding:utf-8
from HTMLParser import HTMLParser

def strip_tags(html):
	from HTMLParser import HTMLParser
    html = html.strip()
    html = html.strip("\n")
    result = []
    parse = HTMLParser()
    parse.handle_data = result.append
    parse.feed(html)
    parse.close()
    return "".join(result)

if __name__ == '__main__':
	a = strip_tags(u'<span id="pub_date">2014dasd10:28</span>')
	print a