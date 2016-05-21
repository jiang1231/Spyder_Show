# -*- coding: utf-8 -*-
from multiprocessing.dummy import Pool as ThreadPool #多线程  
import time  
import urllib2  
  
urls = [  
    'http://www.python.org',   
    'http://www.python.org/about/',  
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',  
    'http://www.python.org/doc/',  
    'http://www.python.org/download/',  
    'http://www.python.org/getit/',  
    'http://www.python.org/community/',  
    'https://wiki.python.org/moin/',  
    'http://planet.python.org/',  
    'https://wiki.python.org/moin/LocalUserGroups',  
    'http://www.python.org/psf/',  
    'http://docs.python.org/devguide/',  
    'http://www.python.org/community/awards/'  
    ]  

def ff(url):
    time.sleep(1)
    print url

if __name__ == '__main__':
        
    # 单线程  
    start = time.time()  
    results = map(ff, urls)  
    print 'Normal:', time.time() - start  
      
    # 多线程  
    start2 = time.time()  
    # 开4个 worker，没有参数时默认是 cpu 的核心数  
    pool = ThreadPool(8)  
    # 在线程中执行 urllib2.urlopen(url) 并返回执行结果  
    results2 = pool.map(ff, urls)  
    pool.close()  
    pool.join()  
    print 'Thread Pool:', time.time() - start2 