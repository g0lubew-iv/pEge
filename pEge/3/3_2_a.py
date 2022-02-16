res = []
for number in range(777, 19990 + 1, 1):
    if max(list(map(int, list(str(oct(number)).replace("0o", ""))))) == 6:
        res.append(number)

print(len(res), max(res) - min(res), sep="\n")
