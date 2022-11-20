import sys
from fractions import Fraction

input = []
for i in sys.stdin:
    input.append(i)
    
rows = int(input[0])
d = []
for i in range(1, rows + 1):
    d.append(input[i].split(' '))    

def calc(a,b,c,d,string):
    if string == '+':
        res = str(Fraction(int(a), int(b)) + Fraction(int(c), int(d))).split('/')
    elif string == '-':
        res = str(Fraction(int(a), int(b)) - Fraction(int(c), int(d))).split('/')
    elif string == '/':
        res = str(Fraction(int(a), int(b)) / Fraction(int(c), int(d))).split('/')
    elif string == '*':
        res = str(Fraction(int(a), int(b)) * Fraction(int(c), int(d))).split('/')

    if len(res) == 1:
        return res[0], 1
    return res[0], res[1]   

result = ''
for i in range(rows):
    l, m = calc(d[i][0], d[i][1], d[i][3], d[i][4], d[i][2])
    result += f'{l} / {m}\n'

print(result)