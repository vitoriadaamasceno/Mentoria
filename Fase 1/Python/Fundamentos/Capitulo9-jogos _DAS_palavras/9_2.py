fin = open('words.txt')

def has_nos_e(word):
    if 'e' in word:
        return True
    else:
        return False

cont=0
contf=0
for line in fin:
    word = line.strip()
    print(has_nos_e(word))
    if has_nos_e(word) == True:
        cont=cont+1
    else:
        contf=contf+1
true=(cont/113809)*100
false=(contf/113809)*100
print('A porcentagem de palavras que contem a letra e é de :', true, '%')
print('A porcentagem de palavras que NÂO contem a letra e é de :',false, '%')