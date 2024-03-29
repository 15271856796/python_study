import multiprocessing as mp

def job(q):
    res=0
    for i in range(100):
        res+=i+i**2+i**3
    q.put(res)


if __name__=='__main__':
    q=mp.Queue()
    p1=mp.Process(target=job,args=(q,))        #和线程的创建和相似
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()           #和线程的用法是一个意思
    p2.join()
    res1=q.get()
    res2=q.get()
    print(res1+res2)