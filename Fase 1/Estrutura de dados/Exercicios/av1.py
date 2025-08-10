'''

Você está desenvolvendo um sistema para consultar o estoque de uma livraria. Os livros estão armazenados com seus respectivos IDs em ordem crescente.

Implemente uma função que receba uma lista ordenada de IDs e um ID de livro a ser buscado. Seu algoritmo deve:

Usar pesquisa binária para encontrar o livro.

Retornar a posição do livro caso exista, ou uma mensagem indicando que ele não está no estoque.


'''

def buscar_livro(ids:list, id):
   baixo = 0
   alto = len(ids) - 1

   while baixo <= alto:
    meio = (baixo + alto) // 2
    valor = ids[meio]

    if valor == id:
      return meio
    elif meio > valor:
      alto = meio - 1
    else:
      baixo = meio + 1
    
   return None

livros = [101, 203, 305, 409, 512]
print(buscar_livro(livros, 512))