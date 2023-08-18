from multiprocessing import Process, current_process
import time
import os 

'''
`ps aux` can be used to find all the running processes.
`ps aux | grep pid` can be used to get specific process with pid.
'''
def task(name):
    # print(f"{current_process().pid} is running.")
    print(f"{os.getpid()} is running.")

    print(f'{name} is running')
    time.sleep(35)
    print(f'{name} is over') 

if __name__ == "__main__":
    p = Process(target=task, args=("my program", ))
    p.start()
    print("main process", os.getpid())
    print("father process", os.getppid())
    
    time.sleep(1)
    
    # Kill a process, which takes some time.
    p.terminate()
    time.sleep(0.1)
    # Check whether process is alive.
    print(p.is_alive())