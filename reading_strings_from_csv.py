import numpy as np
import csv


def csv_to_list():
    data = []
    for line in open('files/data.csv'):
        data.append(line.strip().split(','))
        # strip removes whitespace
    print(f'# using csv_to_list: \n{data}\n')


def convert_to_float():
    data = []
    for line in open('files/data.csv'):
        row = []
        for col in line.strip().split(','):
            row.append(float(col))
        data.append(row)
    print(f'# using convert_to_float: \n{data}\n')


def convert_using_numpy():
    data = []
    for line in open('files/data.csv'):
        data.append(line.strip().split(','))
    data = np.asarray(data, float)
    print(f'# using convert_using_numpy: \n{data}\n ')


def read_convert_using_numpy():
    data = np.loadtxt('files/data.csv', delimiter=',')
    print(f'# using read_convert_using_numpy: \n{data}\n')


def calc_stats(filename):
    data = np.loadtxt(filename, delimiter=',')
    mean = np.round(np.mean(data), 1)
    median = np.round(np.median(data), 1)
    print(f'# using calc_stats: {(mean, median)}')
    return mean, median


def numerical_operations():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(a * b)
    print(a + b)
    print(a * b)
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print(a)
    print(f' first row of the array ')
    print(a[0, :])
    print(a[:, 1])


def mean_datasets(filenames):
    filecount = len(filenames)
    print(filecount)
    data = np.loadtxt(filenames[0], delimiter=',')

    for i in range(1, filecount):
        data += np.loadtxt(filenames[i], delimiter=',')
    return np.round(data / filecount, 1)


if __name__ == '__main__':
    csv_to_list()
    convert_to_float()
    convert_using_numpy()
    read_convert_using_numpy()
    print(calc_stats('files/data3.csv'))
    numerical_operations()
    y = mean_datasets(['mean_datasets/data1.csv', 'mean_datasets/data2.csv', 'mean_datasets/data3.csv'])
    print(y)
    print(mean_datasets(['mean_datasets/data4.csv', 'mean_datasets/data5.csv', 'mean_datasets/data6.csv']))
