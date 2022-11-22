import sys

data = []
num = 1
for i in sys.stdin:
    if num % 2 == 0:
        data.append(i.strip()[1:-1].split('|'))
    num += 1

white = []
black = []

start = 'a'
columns = {i: chr(ord(start) + i) for i in range(0, 8)}
rows = {i:8 - i for i in range(0, 8)}

for r in range(len(data)):
    for c in range(len(data[r])):
        sq = data[r][c][1]        
        if sq != ':' and sq != '.':    
            if sq.isupper():                
                white.append(f'{sq.capitalize()}{columns[c]}{rows[r]}')
            else:                
                black.append(f'{sq.capitalize()}{columns[c]}{rows[r]}')

pieces_in_order = "KQRBNP"

white_list = sorted(sorted(white, key=lambda pos: pos[2], reverse=False), key=lambda pos: [pieces_in_order.index(c) for c in pos[0]])
black_list = sorted(sorted(black, key=lambda pos: pos[2], reverse=True), key=lambda pos: [pieces_in_order.index(c) for c in pos[0]])

white_ans = 'White: '
for i in white_list:
    if i[0] == 'P':
        white_ans += f'{i[1:]},'
    else:
        white_ans += f'{i},'

black_ans = 'Black: '
for i in black_list:
    if i[0] == 'P':
        black_ans += f'{i[1:]},'
    else:
        black_ans += f'{i},'        

print(white_ans[:-1])
print(black_ans[:-1], '\n')
