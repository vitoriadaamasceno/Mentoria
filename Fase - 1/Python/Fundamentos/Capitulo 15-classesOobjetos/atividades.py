'''
Antes de começar vamos entender o que são classes e objetos em Python.


Classes são estruturas que representam objetos, ou seja, são modelos que definem os atributos e métodos que um objeto deve ter.
Objetos são instâncias de classes, ou seja, são variáveis que representam uma classe.

'''

class Circle:
   ''''''
    
class Point:
    ''' Representa um ponto no espaço 2D'''

ponto = Point()
ponto.x = 100.0
ponto.y = 150.0
   
circulo = Circle()
circulo.radius = 75
circulo.center = ponto
print(circulo.radius, circulo.center.x, circulo.center.y)


def point_in_circle(ponto, circulo):
    if ponto.x or ponto.y > circulo.radius:
        return True
    
print(point_in_circle(ponto, circulo))


