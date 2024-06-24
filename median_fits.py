import numpy as np
from statistics import mean, median
import time


def list_stats(data):
    arrlen = len(data)
    mid = int(arrlen / 2)
    my_mean = sum(data) / arrlen

    data.sort()
    if len(data) == 1:
        my_median = data[0]
    elif (arrlen % 2) == 0:
        my_median = (data[mid - 1] + data[mid]) / 2
    else:
        my_median = data[mid]
    print(data)
    print(my_median)
    print(my_mean)
    print("$$$")
    return my_median, my_mean


if __name__ == '__main__':
    data = [1.3, 2.4, 20.6, 0.95, 3.1]
    start = time.perf_counter()
    list_stats(data)
    end = time.perf_counter() - start

    # Run your function with the second example in the question
    m = list_stats([1.5])
    # print(m)

    m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
    # print(m)

    m = list_stats([17.2])
    # print(m)

    # Using statistics
    print(median(data))
    print(mean(data))

    print(end)
