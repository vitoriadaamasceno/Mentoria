teste = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(teste)
#outra forma de fazer
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))