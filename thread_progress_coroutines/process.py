from multiprocessing import Process,current_process
import time

def func():
    time.sleep(10)
    proc = current_process()
    print(proc.name,proc.pid)

if __name__ == '__main__':

    sub_proc = Process(target=func,args = ())
    sub_proc.start()
    sub_proc.join()
    proc = current_process()
    print(proc.name,proc.pid)
    print(sub_proc.name)