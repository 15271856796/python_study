
import multiprocessing as mp
import time

def job(v,num,l):
    l.acquire()             #加锁是为了使在某个进程在用的时候,另一个进程不能用
    for _ in range(10):
        time.sleep(0.1)
        v.value+=num
        print(v.value)
    l.release()

def mulprocess():
    l=mp.Lock()
    value=mp.Value('i',0)           #声明了一个共享的变量的内存,里面的初始值是0
    p1=mp.Process(target=job,args=(value,1,l))
    p2 = mp.Process(target=job, args=(value,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__=='__main__':
    mulprocess()

