class Point: #O objeto de classe é como uma fábrica para criar objetos.
    """ Representa dois pontos """
    
#atribuindo valores a um objeto instanciado
class Retangulo:
    ''' Representa um retângulo'''
    
box = Retangulo()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

print(box.width, box.height, box.corner.x, box.corner.y)

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

print(find_center(box))
