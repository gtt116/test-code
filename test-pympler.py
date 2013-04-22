from pympler.asizeof import asizeof
import sys


l = [1, 2, 3, 4 ,5]

print asizeof(l)
print sys.getsizeof(l)
