from multiprocessing import Process
import time


def task(name):
    print(f'{name} is running')
    time.sleep(5)
    print(f'{name} is over')


if __name__ == "__main__":
    start_time = time.time()
    process_list = []
    for i in range(3):
        p = Process(target=task, args=(f"my program {i}", ))
        p.start()
        process_list.append(p)

    # The main process will always wait until the sub-process finishes.
    for process in process_list:
        process.join()

    end_time = time.time()
    print("main", end_time - start_time)