A, B = 333666, 666999
s = []

for number in range(A, B + 1, 1):
    if not number % 17:
        if sum([1 if x == '7' else 0 for x in str(number)]) == 2:
            s.append(number)

print(len(s), max(s), sep='\n')
