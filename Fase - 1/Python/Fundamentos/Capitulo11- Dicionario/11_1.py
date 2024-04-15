""" Escreva uma função que leia as palavras em words.txt e guarde-as como chaves em um dicionário. Não importa quais são os valores. Então você pode usar o operador in como uma forma rápida de verificar se uma string está no dicionário.

Se fez o Exercício 10.10, você pode comparar a velocidade desta implementação com o operador in de listas e a busca por bisseção. """

def read_words():
    words = dict()
    n=0
    with open('/home/jusbrasil/Mentoria/Fase - 1/Python/Fundamentos/Capitulo11- Dicionario/words2.txt', 'r') as file:
        for line in file:
            word = line.strip()
            words[word] = n
            n += 1
    return words

print(read_words())
