for _ in range(int(input())):
    a, b = map(int, input().split())
    index = max(a, b)
    print((a - b) * (-1) ** index + index * index - index + 1)
