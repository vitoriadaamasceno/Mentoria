def cumsum(t):
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res

t = [1, 2, 3]
print(cumsum(t))
