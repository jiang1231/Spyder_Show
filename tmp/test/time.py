import time

if __name__ == '__main__':
	time_now = time.time()
	time_now = int(time_now)
	with open('time.txt','w') as file:
		file.write(str(time_now))
	# with open('time.txt','wr') as file:
	# 	file.read()
	time.sleep(5)
	with open('time.txt','r') as file:
		spider_time = file.readline()
	print spider_time
	time_now = time.time()
	time_now = int(time_now)-int(spider_time)
	print time_now

