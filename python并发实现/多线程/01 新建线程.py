import threading
import time

def thread_job():
    #time.sleep(2)
    print('this id an added Thread,number is %s' %threading.current_thread())

def main():
    # target是线程需要完成的功能模块,如果函数有参数的话,在建进程时候还要传参,用args进行传参
    added_thread=threading.Thread(target=thread_job)
    added_thread.start()
    #输出所有线程的数量(不管有没有运行完)
    print(threading.active_count())
    #输出所有正在运行的线程的名称(已经执行完的进程不进行打印)
    print(threading.enumerate())
    #输出当前正在运行的线程
    print(threading.current_thread())

if __name__=='__main__':
    main()