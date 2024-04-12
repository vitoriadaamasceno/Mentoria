def uses_all(word,letters):
    for let in letters.replace(' ',''):
        if let not in word:
            return False
    return True
palavra='hoe alfalfa?'

letters='acefhlo?'

print(uses_all(palavra,letters))

