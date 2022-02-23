def f(k, n):
    res = 0
    if not n:
        return res + 1
    elif k < n:
        for i in range(k + 1, n + 1):
            res += f(i, n - i)
        return res
    return res


print(f(0, int(input())))
