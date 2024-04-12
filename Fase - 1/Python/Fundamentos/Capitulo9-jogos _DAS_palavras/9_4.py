#Escreva uma função chamada uses_only que receba uma palavra e uma série de letras e retorne True, se a palavra só contiver letras da lista. Você pode fazer uma frase usando só as letras acefhlo? Que não seja “Hoe alfalfa?”



def uses_only(word,letters):
    for let in word.replace(' ',''):
        if let not in letters:
            return False
    return True

palavra='hoe alfalfa?'

letters='acefhlo?'

print(uses_only(palavra,letters))