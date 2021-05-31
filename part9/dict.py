import os
import glob
from math import sqrt

file_sizes = { os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}

# print(file_sizes)
# print(range(2, int(sqrt(12)) + 1))
print(sqrt(12))
for i in range(2, int(sqrt(12)) + 1):
  print (i)
