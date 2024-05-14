def get_count(sentence):
    total=[]
    sentence=sentence.strip()
    vogais=['a','e','i','o','u']
    for i in sentence:
        for v in vogais:
            if i==v:
                total.append(i)
    print(total)
    return len(total)
    
print(get_count('aeiou')) #5