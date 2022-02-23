data = list(map(int, open("INPUT.TXT", mode="r", encoding="utf-8").read().split('\n')[1].split()))
res = []

for x in set(data):
    s = []
    for i in data:
        if i == x:
            s.append([])
        elif len(s):
            s[-1].append(i)
    for m in list(filter(lambda r: r, s[:-1])):
        res.append(len(m) + 1)

print(max(res)) if res else print(1)
