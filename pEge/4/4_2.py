data = list(map(int, open("17-243.txt", mode="r", encoding="utf-8").read().split("\n")[:-1]))
x_number = sum(list(map(lambda y: sum(list(map(int, list(str(y))))), list(filter(lambda x: not x % 33, data)))))
res = list(filter(lambda c: c[0] > x_number or c[1] > x_number,
                  [(data[i], data[i + 1]) for i in range(len(data) - 1)]))
print(len(res), min(list(map(lambda m: sum(m), res))), sep="\n")
