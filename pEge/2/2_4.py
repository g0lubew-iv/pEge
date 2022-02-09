A, B = 1476, 7039
s = []

for number in range(A, B + 1, 1):
    if (not (number % 2)) and (number % 16):
        if int(str(number)[-2]) >= 4:
            s.append(number)

print(len(s), max(s), sep='\n')
