exe1 = " maria jose alana bruna"
print(exe1.upper())
print(exe1.title())
print(exe1.capitalize())    
print(exe1.lower()) # Converte todas as letras para minúsculas
print(exe1.swapcase()) # Troca as letras maiúsculas por minúsculas e vice-versa
print(exe1.strip()) # Remove os espaços em branco do início e do final da string
print(exe1.lstrip()) # Remove os espaços em branco do início da string
print(exe1.replace(' ','-'))


#8_2
string = "bbanana"
print(string.count('a')) # Conta quantas vezes a letra 'a' aparece na string
print(string.find('a'))    # Retorna a posição da primeira ocorrência da letra 'a'

#8_3
fruit = 'banana'
fruit[0:5:2]

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('arara'))

#8_4

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

print(any_lowercase1('Anitaa'))

#8_5

#CIFRA CESAR
def rotate_word(word, n):
    new_word = ''
    for letter in word:
        new_word += chr(ord(letter) + n)
    return new_word

print(rotate_word('IBM', -1))