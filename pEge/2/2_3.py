A, B = 4563, 7912
s = []

for number in range(A, B + 1, 1):
    if not number % 7:
        if int(str(number)[-1]) + int(str(number)[0]) > 10:
            s.append(number)

print(len(s), max(s), sep='\n')
