def avoid(word):
    letra =input()
    letters=[]
    letters.append(letra)
    cont=0
    for let in letters:
        if let in word:
            cont+=1
    if cont>0:
        return False
    else:
        return True




palavra='olho viu boca piu'


print(avoid(word=palavra))

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

