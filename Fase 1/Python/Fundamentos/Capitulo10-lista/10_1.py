def nested_sum(t):
    total = 0
    for x in t:
        total += x
    return total

t = [[1, 2], [3], [4, 5, 6]]
nested_sum(t)
print(nested_sum(t))

