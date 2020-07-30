from operator import mul, add
from functools import reduce

fac = reduce(mul, range(1, 9))
sum = reduce(add, range(-8, 0))
result = fac - sum
print(result)
