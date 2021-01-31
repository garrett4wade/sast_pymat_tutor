import threading
import numpy as np


class MyThread:  # you need to inherit threading.Thread
    def __init__(self):  # you may add some other arguments
        pass

    def run(self):
        # run some cpu-bound task, i.e. numpy array computation
        arr = np.random.randn(64)
        while True:
            arr2 = arr**2
            arr = (arr2 - np.mean(arr2)) / (np.std(arr2) + 1e-8)


if __name__ == "__main__":
    # write something to record the time consumption
    thds = [MyThread() for _ in range(10)]
    for thd in thds:
        thd.start()
    for thd in thds:
        thd.join()

    # write a single-threaded task that runs your task 10 times
    # record the time and compare it with the previous one
    pass
