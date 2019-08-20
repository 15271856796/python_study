#进程池的意思是说要需要处理的任务放在进程池中,那么Python会为你自动的分配进程等

import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    pool=mp.Pool(processes=2)
    res=pool.map(job,range(10))
    print(res)

if __name__=='__main__':
    multicore()