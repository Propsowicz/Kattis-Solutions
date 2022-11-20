import sys

data = []
for i in sys.stdin:
    data.append(i.strip())
coord_lists = []
i = 0
while i < len(data):
    if not ' ' in data[i]:
        if i > 0:
            coord_lists.append(temp_data)
        temp_data = []
    else:   
        temp_data.append(data[i].split(' '))
    i += 1

result = ''
for i in range(len(coord_lists)):
    area = 0   
    clockwise_sum = 0
    for j in range(len(coord_lists[i])):
        area += ((int(coord_lists[i][j - 1][0]) * int(coord_lists[i][j][1]) - int(coord_lists[i][j - 1][1]) * int(coord_lists[i][j][0]))) / 2    
        clockwise_sum += (int(coord_lists[i][j][0]) - int(coord_lists[i][j - 1][0])) * (int(coord_lists[i][j][1]) + int(coord_lists[i][j - 1][1]))
    clock_str = 'CW' if clockwise_sum > 0 else 'CCW'
    result += f'{clock_str} {abs(area)}\n'

print(result)