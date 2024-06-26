#Herançaa simples
""" class A:
    pass

class B (A):
    pass


#Herança multipla 

class C(A,B):
    pass """

class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())


class Bar(Foo):
    def hello(self):
        return super().hello()


bar = Bar()
bar.hello()