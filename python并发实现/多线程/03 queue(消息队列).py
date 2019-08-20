import threading
import time
from queue import Queue

def job(l,q):
    for i in range(len(l)):
        l[i]=l[i]**2
    #消息入队
    q.put(l)

def multithreading():
    #因为线程不能有返回值,所以把计算结果可以存在消息队列Queue中
    q=Queue()
    threads=[]
    data=[[1,2,3],[4,5,6],[8,9,10],[5,5,5]]
    for i in range(4):
        t=threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    result=[]
    for _ in range(4):
        #消息出队,一个个获取
        result.append(q.get())
    print(result)



if __name__=='__main__':
    multithreading()            #[[1, 4, 9], [16, 25, 36], [64, 81, 100], [25, 25, 25]]
