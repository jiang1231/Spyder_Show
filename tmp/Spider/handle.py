#conding:utf-8
import sqlite3
'''
[(u'Content',), (u'DownloadFile',), (u'sqlite_sequence',)]
content
title,link,orgain,content,keywords,PageUrl
'''
def read_txt(txtPath, coding = 'utf-8'):
    import codecs
    f = codecs.open(txtPath,'r',coding).readlines()
    f[0] = f[0].replace(u"\ufeff",u"")
    dataset = []
    for line in f:
        line = line.replace("\r\n","")
        line = line.replace("\n","")
        dataset.append(line)
    return dataset

def dataset():
	cx = sqlite3.connect('nohandle.db3')
	cur = cx.cursor()
	# cur.execute("select * from table")  
	# col_name_list = [tuple[0] for tuple in cur.description]  
	# print col_name_list


	# cur.execute("PRAGMA table_info(table)")  
	# print cur.fetchall()
	cur.execute("select name from sqlite_master where type='table' order by name")
	result = cur.fetchall()
	print result
	cur.execute("select * from Content")
	col_name_list = [tuple[0] for tuple in cur.description] 
	print col_name_list
	# a = cur.execute('select id, title from Content')
	# for i in a:
	# 	print i
	cur.execute("PRAGMA table_info(Content)") 
	print cur.fetchall() 

	info = cur.execute('select title,link,orgain,content,keywords from Content')
	result = []
	k=[]
	keywords = read_txt('keywords_back.txt')
	for i in info:
		if len(i[0]) != 0 and len(i[1]) != 0 and len(i[2]) != 0 and len(i[3]) != 0:
			if i[4] in keywords:
				result.append(i)
				k.append(i[1])
	print len(result),len(k),len(set(k))
	print result[0]
	return result	


if __name__ == '__main__':
	dataset()




