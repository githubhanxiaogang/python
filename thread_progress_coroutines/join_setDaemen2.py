# setDaemon()方法。主线程A中，创建子线程B，并且在主线程A中调用了setDaemon()，这个意思就是，把主线程A设置为守护线程，
# 这时候，要是主线程A执行结束了，就不管子线程B是否完成，一并和主线程A退出。这就是setDaemon方法的含义，基本与join是相反的。
# 此外，还有个要特别注意的：必须在start()方法调用之前设置，如果不设置为守护线程，程序会被无限挂起。
import threading
import time

class MyThread(threading.Thread):
    def __init__(self,id):
        super(MyThread, self).__init__()
        self.id = id
    def run(self):
        time.sleep(5)
        print(999)
        print("This is " + self.getName())

if __name__ == '__main__':
    t1 = MyThread(999)
    t1.setDaemon(True)
    t1.start()
    print("I am the father thread")
'''
可以看出，子线程t1 中的内容并未打印。
解释：t1.setDaemon(True)的操作，将父线程设置为守护线程。根据setDaemon（）方法的含义，
父线程打印内容后便结束了，不管子线程是否执行完毕了。

程序运行中，执行一个主线程，如果主线程又创建一个子线程，主线程和子线程就分兵两路，分别运行，
那么当主线程完成想退出时，会验证子线程是否完成。如果子线程未完成，则主线程会等待子线程完成后
再退出。但是有时候我们需要的是，只要主线程完成了，不管子线程是否完成，都要和主线程一起退出，
这是就可以用setDemon方法了。

所以，join 和setDaemon方法基本上相反。
'''

