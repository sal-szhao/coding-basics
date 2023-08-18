'''
Two ways of creating a process in python.
'''

from multiprocessing import Process
import time

# First method.
def task(name):
    print(f'{name} is running')
    time.sleep(5)
    print(f'{name} is over')

# Second method.
class MyProcess(Process):
    def run(self):
        print("process is running")
        time.sleep(5)
        print("process is over")

# In windows, creating process must be done in the main function.
if __name__ == "__main__":
    p = Process(target=task, args=("my program", ))
    # p = MyProcess()
    p.start()
    print("main")