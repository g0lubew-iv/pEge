n, m, d, k = map(int, open("INPUT.TXT", mode="r", encoding="utf-8").read().split())

print(n * d * k + m * d * k - d * d * n * m)
