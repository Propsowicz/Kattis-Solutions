import sys

data = []
for i in sys.stdin:
    data.append(i.strip().split(' '))

answer = ''

for a in range(len(data)):
    answer += f'{abs(int(data[a][0]) - int(data[a][1]))}\n'

print(answer)