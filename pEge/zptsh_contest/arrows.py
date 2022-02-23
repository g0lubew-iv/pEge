data = open("INPUT.TXT", mode="r", encoding="utf-8").read()

# print(data.count(">>-->") + data.count("<--<<"))
print(len([i for i in range(len(data)) if data.startswith(">>-->", i)]) +
      len([i for i in range(len(data)) if data.startswith("<--<<", i)]))
