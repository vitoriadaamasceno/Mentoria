from __future__ import print_function, division

import bisect


def make_word_list():
    # lEIA O ARQUIVO words.txt  
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list

def in_bisect(word_list, word):
    # Verifica se a palavra está na lista
    #bisect_left retorna o índice onde um determinado elemento deve ser inserido para manter a ordem da lista
    #bisect_right retorna o índice onde um determinado elemento deve ser inserido para manter a ordem da lista
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect(word_list, word))