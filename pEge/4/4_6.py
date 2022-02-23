from itertools import chain

divs = lambda n: chain(*((d, n // d) for d in range(1, int(n ** 0.5) + 1) if not n % d))

for number in range(135790, 163228 + 1, 1):
    if sum(sorted(set(divs(number)))[1:-1]) > 460000:
        print(len(sorted(set(divs(number)))[1:-1]), sum(sorted(set(divs(number)))[1:-1]))
