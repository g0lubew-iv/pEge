def count(ss):
    s = "$#" + "#".join(ss)+"#"
    p = [0] * len(s)
    m = 0
    r = -1
    for i in range(len(s)):
        k = 1 if i > r else min(p[m + r - i], r - i + 1)
        while i + k < len(s) and i - k >= 0 and s[i + k] == s[i - k]:
            k += 1
        p[i] = k
        if i + k - 1 > r:
            m = i - k + 1
            r = i + k - 1
    return sum([x // 2 for x in p])


print(count("omax"))
