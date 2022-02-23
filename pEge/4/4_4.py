from itertools import chain

divs = lambda n: chain(*((d, n // d) for d in range(1, int(n ** 0.5) + 1) if not n % d))

for number in range(180131, 180179 + 1, 1):
    if len(set(divs(number))) == 6:
        print(*sorted(set(divs(number))))
