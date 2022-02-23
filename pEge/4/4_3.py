data = list(map(int, open("17-243.txt", mode="r", encoding="utf-8").read().split("\n")[:-1]))
st_middle = sum(list(filter(lambda n: n > 0, data))) / len(list(filter(lambda n: n > 0, data)))
res = list(filter(lambda x: x[0] > st_middle or x[1] > st_middle,
                  [(data[i], data[i + 1]) for i in range(len(data) - 1)]))
print(len(res),
      max(list(map(lambda r: r[0] if r[0] > r[1] else r[1],
                   list(map(lambda y: (sum(list(map(int, list(str(y[0]))))),
                                       sum(list(map(int, list(str(y[1])))))), res))))))
