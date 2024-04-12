def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
h = histogram('brontosaurus')

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
#print(eng2sp)

#loops com dicionários

def print_hist(h):
    for c in sorted(h):
        print(c, h[c])
        
print(print_hist(h))
