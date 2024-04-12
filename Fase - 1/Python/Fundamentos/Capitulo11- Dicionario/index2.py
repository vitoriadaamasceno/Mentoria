#Busca reversa
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres','três': 'tres'}

#print(reverse_lookup(eng2sp, 'tres'))


def invert_dict(d):
    inverse = dict() #cria um dicionário vazio
    for key in d: #para cada chave em d
        val = d[key] #val recebe o valor da chave
        if val not in inverse: #se o valor não estiver em inverse
            inverse[val] = [key] #cria uma lista com a chave
        else:#se o valor já estiver em inverse
            inverse[val].append(key)#adiciona a chave na lista
    return inverse

def example3():
    global count
    count += 1