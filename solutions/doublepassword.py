import sys

data = []

for i in sys.stdin:
    data.append(i)
    
result = 1
for i in range(len(data[0])):
    if data[0][i] == data[1][i]:
        result *= 1
    else:
        result *= 2

print(result)