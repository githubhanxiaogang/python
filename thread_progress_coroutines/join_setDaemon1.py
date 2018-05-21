#join()方法：主线程A中，创建子线程B，并且在主线程A中调用B.join(),那么，主线程A会在调用的地方等待，
# 直到子线程B完成操作后，才可以接着往下执行，那么在调用这个线程可以使用被调用线程的join方法。
# 原型：join([timeout])
# 代表线程运行的时间，即如果超过这个时间，不管这个此线程有没有执行完毕都会被回收，然后主线程或函数都会被接着执行。


import threading
import time

class MyThread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        # super(MyThread, self).__init__()
        self.id = id

    def run(self):
        time.sleep(2)
        print(self.id)

if __name__ == '__main__':
    t1 =MyThread(999)
    t1.start()
    # t1.join()  #有没有join
    for i in range(5):
        print(i)

