1. GET .../paises/55/estados/11/cidades/100
R: status 200
Response: Santos, 1000


2. R: ctatus 200
Reponse  100,Santos e 200 São Vicente

3. 200
Reponse: 300 Belo Horizonte em formato array( possibilidade de vim mais de um resultado.)

4. 200
Response: array com Belo Horizonte


5.  201
Reponse : Cotia + id
Location  com novo endereço

6. 200 ou 204 No content ( caso não queria retornar nada)
Response: Campo alterado

7. 404 Not Found
Response : mensagem indicando que não foi encontrado

8. 404 Not Found
Response : mensagem indicando que não foi encontrado

9. 404 Not Found
Response : mensagem indicando que não foi encontrado 

10. 200
Reponse: caso você use query params e o valor não exista deve ser retornado 200 pois a pesquisa foi feita e uma lista vazia indicando que não foi encontrado.

11. 400 Bad request
Se o query params não existir o melhor é retornar 400 já que é um erro do cliente.
