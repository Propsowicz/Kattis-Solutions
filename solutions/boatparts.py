import sys

data = []
for i in sys.stdin:
    data.append(i)

d = data[0].split(' ')
total_parts = int(d[0])
free_days = int(d[1])

buyed_parts = []

for i in range(1, len(data)):
    buyed_parts.append(data[i])

def maintance(total_parts, free_days, buyed_parts):
    stack = []
    day = 0

    while day < free_days:
        if buyed_parts[day] not in stack:
            stack.append(buyed_parts[day])
        day += 1        
        if len(stack) == total_parts:
            return day
        
    return 'paradox avoided'

print(maintance(total_parts, free_days, buyed_parts))