

#锁只有一个,只有拿到锁之后才能执行那块代码,
# 等到别人用完释放后,你才能抢到锁后往下执行代码,没有锁的时候你就只能等着
#不在锁范围内的代码不受影响
import threading

def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=10
        print("job1",A)
    lock.release()
def job2():
    global A,lock
    print(2222)
    lock.acquire()
    for i in range(10):
        A+=1
        print('job2',A)
    lock.release()

if __name__=='__main__':
    lock=threading.Lock()
    A=0
    thread1=threading.Thread(target=job1)
    thread2=threading.Thread(target=job2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


