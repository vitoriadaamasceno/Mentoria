def only_upper(t):
    res = []
    for s in t:
        if s.islower():
            res.append(s)
    return res

print(only_upper('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'))


def some_list(t):
    res = []
    for x in t:
        res.append(sum(x))
    return res

letras= ['m', 'a', 'r', 'c', 'o']
some_list(letras)