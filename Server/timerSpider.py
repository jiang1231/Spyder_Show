from apscheduler.schedulers.blocking import BlockingScheduler
import os
import spider

def main():
    sched = BlockingScheduler()
    sched.add_job(spider.spider(), 'interval', seconds=21600)
    print 'Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C')

    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == '__main__':
	main()
