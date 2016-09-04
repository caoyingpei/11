from multiprocessing import Pool
import multiprocessing
import time, random
 
def write(q,lock):
    lock.acquire()
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)        
        q.put(value)        
    lock.release()
 
def read(q):
    while True:
        if not q.empty():
            value = q.get(False)
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        else:
            break
 
if __name__=='__main__':
    manager = multiprocessing.Manager()
    q = manager.Queue()
    #progress queue lock
    lock = manager.Lock() 
    p = Pool()
    pw = p.apply_async(write,args=(q,lock))    
    pr = p.apply_async(read,args=(q,))
    p.close()
    p.join()
    
    print('done!')