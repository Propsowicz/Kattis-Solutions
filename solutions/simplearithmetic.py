from decimal import *
from fractions import *

data = input().strip().split(' ')
a = int(data[0])
b = int(data[1])
c = int(data[2])
getcontext().prec = int(pow(10, 3) + 1)
res_1 = Decimal(a * b)

if c == 1:
    result = res_1
else:
    result = Decimal(res_1 / c)
print(result)