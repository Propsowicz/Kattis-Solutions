import sys
from sys import setrecursionlimit
setrecursionlimit(10001)

data = []
for i in sys.stdin:
    data.append(i.strip())
drawing_repr = []
i = 0
while i < len(data):
    if ' ' in data[i]:
        temp_data = []
        temp_data.append(data[i].split(' '))
        tt_data = []
        for j in range(int(temp_data[0][0])):
            i += 1
            tt_data.append(list(data[i]))
        temp_data.append(tt_data)            
        drawing_repr.append(temp_data)
    i += 1

def check(data, y, x, ymax, xmax):
    if y < 0 or y > ymax or x < 0 or x > xmax:
        return None
    elif data[y][x] == '-':    
        data[y][x] = '#'
        check(data, y+1, x, ymax, xmax)
        check(data, y-1, x, ymax, xmax)
        check(data, y, x+1, ymax, xmax)
        check(data, y, x-1, ymax, xmax)  

result = ''
for k in range(len(drawing_repr)):
    checked_list = []
    lines = int(drawing_repr[k][0][0])
    string = int(drawing_repr[k][0][1])
    data = drawing_repr[k][1]
    
    star_counter = 0
    for y in range(lines):
        for x in range(string):
            if data[y][x] == '-':
                check(data, y, x, lines - 1, string - 1)
                star_counter += 1
    result += f'Case {k + 1}: {star_counter}\n'

print(result)
