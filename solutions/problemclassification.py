import sys

data_raw = []
for i in sys.stdin:
    data_raw.append(i)
    
data = []
for i in range(len(data_raw)):
    data.append(data_raw[i].replace('\n', ''))
    
number_of_cat = int(data[0])
words_data = [data[i].split(' ') for i in range(1, number_of_cat + 1)]
categories = []
for i in range(len(words_data)):
    categories.append(words_data[i][0])
    words_data[i].pop(0)
    words_data[i].pop(0)

string = ''
for i in range(number_of_cat + 1, len(data)):
    string += f' {data[i]}'

    
str_data = string.split(' ')
counter = [0] * number_of_cat

for i in range(len(str_data)):
    for j in range(number_of_cat):
        if str_data[i] in words_data[j]:
            counter[j] += 1

sorted_cat = [y for _,y in sorted(zip(counter, categories),key=lambda x: x[0], reverse=True)]
sorted_count = sorted(counter, reverse=True)

result = []
for i in range(number_of_cat):
    if sorted_count[i] != sorted_count[i - 1] and i > 0:
        break
    result.append(sorted_cat[i])
result.sort()

    
answer = ''
for i in range(len(result)):
    answer += f'{result[i]}\n'
print(answer)
