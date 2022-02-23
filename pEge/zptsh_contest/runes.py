import re

data = open("INPUT.TXT", mode="r", encoding="utf-8").read().replace("\n", "")
words = re.findall(r"[A-Z][a-z]{1,3}", data)

with open("OUTPUT.TXT", mode="w", encoding="utf-8") as res:
    res.write("Yes" if "".join(words) == data else "No")
