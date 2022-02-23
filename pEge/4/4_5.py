from itertools import chain

divs = lambda n: chain(*((d, n // d) for d in range(1, int(n ** 0.5) + 1) if not n % d and d % 2))

for number in range(190061, 190080 + 1, 1):
    if len(set(divs(number))) == 4:
        print(*sorted(set(divs(number)), reverse=True))
