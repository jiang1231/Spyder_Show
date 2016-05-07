#cooding:utf-8
import time,MySQLdb
'''
database->news
table->news
+-------------+---------+------+-----+---------+----------------+
| Field       | Type    | Null | Key | Default | Extra          |
+-------------+---------+------+-----+---------+----------------+
| id          | int(11) | NO   | PRI | NULL    | auto_increment |
| title       | text    | NO   |     | NULL    |                |
| sports_kind | text    | NO   |     | NULL    |                |
| team        | text    | NO   |     | NULL    |                |
| content     | text    | NO   |     | NULL    |                |
| time        | text    | YES  |     | NULL    |                |
+-------------+---------+------+-----+---------+----------------+
'''



if __name__ == '__main__':
	conn = MySQLdb.connect(host='119.29.157.174', user='root', 
							passwd='yinruyi',db='news')
	cursor = conn.cursor()
	cursor.execute('show databases;')
	for data in cursor.fetchall():
		print data
	cursor.close()
	conn.commit()
	conn.close()
