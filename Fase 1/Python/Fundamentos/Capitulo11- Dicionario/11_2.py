
def invert_dict(d):
    inverse = dict() #cria um dicionário vazio
    for key in d: #para cada chave em d
        val = d[key] #val recebe o valor da chave
        if val not in inverse: #se o valor não estiver em inverse
            inverse[val] = [key] #cria uma lista com a chave
        else:#se o valor já estiver em inverse
            inverse[val].append(key)#adiciona a chave na lista
    return inverse

def invert_dict2(d):
    inverse = dict() #cria um dicionário vazio
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse
       


eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres','três': 'tres'}
print(invert_dict2(eng2sp))