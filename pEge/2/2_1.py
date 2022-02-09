import math

A, B = 8800, 55535
s = []

for number in range(A, B + 1, 1):
    if math.prod(list(map(int, str(number)))) == 35:
        if '7' in str(number):
            s.append(number)

print(len(s), max(s), sep='\n')
