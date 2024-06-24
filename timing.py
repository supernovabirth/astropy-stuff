import numpy as np
import time

n = 10**7
data = np.random.randn(n)

start = time.perf_counter()
mean = sum(data)/len(data)
seconds = time.perf_counter() - start

print('Calculating on my own took {:.2f} seconds.'.format(seconds))

start = time.perf_counter()
mean = np.mean(data)
seconds = time.perf_counter() - start

print('Using Numpy took {:.2f} seconds.'.format(seconds))