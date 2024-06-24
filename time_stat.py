import statistics

import numpy as np
import time


def time_stat(func, size, ntrials):
    total_time = 0
    for i in range(ntrials):
        data = np.random.randn(size)
        start = time.perf_counter()
        func(data)
        end = time.perf_counter() - start
        total_time += end
    return total_time / ntrials


if __name__ == '__main__':
    print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10 ** 5, 10)))
    print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10 ** 5, 1000)))
