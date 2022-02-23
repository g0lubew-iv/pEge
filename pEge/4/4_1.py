data = list(map(int, open("17-243.txt", mode="r", encoding="utf-8").read().split("\n")[:-1]))
s = [(data[i], data[i + 1]) for i in range(len(data) - 1)]
max_number = max(list(filter(lambda y: not y % 153, data)))
res = list(filter(lambda x: (x[0] > max_number or x[1] > max_number and
                             ("1111" in str(bin(x[0])) or "1111" in str(bin(x[1]))), s), s))
print(len(res), min(list(map(lambda x: sum(x), res))), sep="\n")
