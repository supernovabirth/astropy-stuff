import sys
import numpy as np

a = np.array([])
b = np.array([1, 2, 3])
c = np.zeros(10**6)

for obj in [a, b, c]:
  print('sys:', sys.getsizeof(obj), 'np:', obj.nbytes)

d = np.zeros(5, dtype=np.int32)
e = np.zeros(5, dtype=np.float64)

print("------------")
for obj in [d, e]:
  print('nbytes         :', obj.nbytes)
  print(f'{obj} obj.size {obj.size} ... obj.itemsize {obj.itemsize}')
  print('size x itemsize:', obj.size * obj.itemsize)

print("------------")
f = [0, 0, 0, 0, 0]
g = [0., 0., 0., 0., 0.]

for obj in [f, g]:
  print('nbytes         :', obj.__sizeof__())
  print(f'{obj} obj.size {obj.__sizeof__()} ... obj.itemsize {obj.__len__()}')
  print('size x itemsize:', obj.__sizeof__() * obj.__len__())