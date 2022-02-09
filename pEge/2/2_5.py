A, B = 2476, 7857
s = []

for number in range(A, B + 1, 1):
    if (not (number % 2)) and (number % 8):
        if int(str(number)[-3]) <= 7:
            s.append(number)

print(len(s), max(s), sep='\n')
