import time
from multiprocessing import Process, Manager
import os


class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1


def find_pythagorean_triplets(start_point, end_point, nn, increase_amount, pythagorean_triplets):
    for x in range(start_point, end_point, increase_amount):
        for y in range(x, nn):
            for z in range(y+1, nn):
                if (x * x) + (y * y) == (z * z):
                    pythagorean_triplets.append([x, y, z])


if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    n = 1000
    triangles = Manager().list()
    processes = []
    for i, start_point in zip(range(1, os.cpu_count()+1)[::-1], range(1, os.cpu_count()+1)):
        end_point = n - os.cpu_count() + i
        processes.append(Process(target=find_pythagorean_triplets,
                                 args=(start_point, end_point, n, os.cpu_count(), triangles)))

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    for i in triangles:
        print(i)
    print(f"Time = {tt.toc()}")
    print(len(triangles))
