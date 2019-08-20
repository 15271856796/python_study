import multiprocessing as mp
import time


def job(a,b):
    time.sleep(2)
    print('aaaa')

if __name__=='__main__':
    p1=mp.Process(target=job,args=(1,2))        #和线程的创建和相似
    p1.start()
    p1.join()           #和线程的用法是一个意思