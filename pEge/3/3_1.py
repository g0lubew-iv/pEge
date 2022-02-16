with open("17-1.txt", mode="r", encoding="utf-8") as f:
    data = list(map(lambda x: int(x.strip()), f.readlines()))

res = []

for i in range(len(data) - 2):
    a, b, c = data[i], data[i + 1], data[i + 2]
    if str(a)[-1] == '6' or str(b)[-1] == '6' or str(c)[-1] == '6':
        if a < ((a + b + c) / 3) or b < ((a + b + c) / 3) or c < ((a + b + c) / 3):
            res.append(a + b + c)

print(len(res), max(res), sep="\n")
