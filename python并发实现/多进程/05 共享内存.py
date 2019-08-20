#进程之间没有办法像线程那样直接共享变量的值,只能共享内存

import multiprocessing as mp
value=mp.Value('d',1)             #声明了一个值的内存用以共享,'d' 是存的数据的类型,1是对应所存的值
array=mp.Array('i',[1,2,3])       #声明了一个列表的内存用以共享

#具体的应用在第六节的锁