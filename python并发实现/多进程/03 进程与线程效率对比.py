
#在单核中多进程或者多线程并不一定会比单进程快,因为多进程有状态切换,资源消耗等,并不一定就比单进程的快

import multiprocessing as mp
import threading
import time

def job(q):
    res=0
    for i in range(100000):
        res+=i+i**2+i**3
    q.put(res)

def mulprocess():
    q=mp.Queue()
    p1=mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1 + res2)


def multhread():
    q=mp.Queue()
    t1=threading.Thread(target=job,args=(q,))
    t2 = threading.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1 + res2)

def normal():
    res=0
    for _ in range(2):
        for i in range(100000):
            res+=i+i**2+i**3
    print('normal:',res)



if __name__=='__main__':
    st=time.time()
    normal()
    st1=time.time()
    print('normal time:',st1-st)
    multhread()
    st2=time.time()
    print('thread:',st2-st1)
    mulprocess()
    st3=time.time()
    print("process:",st3-st2)

