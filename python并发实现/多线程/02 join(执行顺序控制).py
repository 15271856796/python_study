import threading
import time

def thread_job():
    print('T1 start\n')
    time.sleep(2)
    print('t1 finish\n')


def main():
    added_thread=threading.Thread(target=thread_job,name='t1')
    added_thread.start()
    #有些时候必须是在某个线程执行结束之后再执行另一个线程,这里join就是指added_thread执行结束后,我们再执行下面的
    added_thread.join()         #虽然说主线程执行结束后子线程还是可以接着执行,但是有些时候要求就是主线程要最后执行完
    print('all done\n')

if __name__=='__main__':
    main()