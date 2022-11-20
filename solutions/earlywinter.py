import sys

data = []
for i in sys.stdin:
    data.append(i)

d = data[0].split(' ')
data_count = int(d[0])
this_year = int(d[1])

d = data[1].split(' ')

hist_data = [int(d[i]) for i in range(len(d))]

def early_snow(data_count, this_year, hist_data):
    i = 0

    while i < data_count:
        if hist_data[i] <= this_year:
            return f"It hadn't snowed this early in {i} years!"
        i += 1
    return "It had never snowed this early!"

print(early_snow(data_count, this_year, hist_data))