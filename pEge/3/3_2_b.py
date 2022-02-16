res = []
for number in range(777, 19990 + 1, 1):
    if (not number % 13 or not number % 11) and number % 15:
        res.append(number)

print(len(res), max(res) - min(res), sep="\n")
