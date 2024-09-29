class Foo:
    def __init__(self, x=None):
        self._x = x
        
    @property #pega um metodo e transforma em propriedades
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, valor):
        self._x += valor
        
    @x.deleter
    def x(self):
        self._x = - 1
        
foo = Foo(10)
print(foo.x) #nao podemos setar diretamente o valor de x sem criar um metodo setter
foo.x = 5
print(foo.x)
del foo.x
print(foo.x)