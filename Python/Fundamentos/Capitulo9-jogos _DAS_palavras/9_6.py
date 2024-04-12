def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

print(is_abecedarian('abdest')) #True

print(is_abecedarian('abdesta')) #False