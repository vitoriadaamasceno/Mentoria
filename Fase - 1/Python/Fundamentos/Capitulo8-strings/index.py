""" fruit = 'banana'
letter = fruit[1]
print(letter)

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    print(letter + suffix)
    
    
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return-1

print(find('banana', 'a')) """

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
