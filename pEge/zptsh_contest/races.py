n, cars = int(input()), list(map(int, input().split()))

for _ in range(int(input())):
    x = int(input()) - 1
    cars[x], cars[x - 1] = cars[x - 1], cars[x]

print(" ".join(list(map(str, cars))))
