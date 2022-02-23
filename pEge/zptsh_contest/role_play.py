n, m, k = map(int, open("INPUT.TXT", mode="r", encoding="utf-8").read().split())

with open("OUTPUT.TXT", mode="w", encoding="utf-8") as res:
    if m < k:
        res.write(str(n * m))
    else:
        res.write(str(((k - 1) + m // k) * n))
