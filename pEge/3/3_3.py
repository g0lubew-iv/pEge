with open("17-1.txt", mode="r", encoding="utf-8") as f:
    data = list(map(lambda x: int(x.strip()), f.readlines()))

res = []

for i in range(len(data) - 1):
    a, b = data[i], data[i + 1]
    if (not a % 9 and str(oct(b))[-1]) == "3" or (not b % 9 and str(oct(a))[-1]):
        res.append(a)
        res.append(b)

print(len(res), max(res), sep="\n")
