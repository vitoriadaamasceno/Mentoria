class Animal:
    def __init__(self, patas):
        self.patas = patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}:{valor}' for chave, valor in self.__dict__.items()])}"

class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)
        
    def __str__(self):
        return 'ave'

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)
    
    def __str__(self):
        return 'mamifero'

class FalarMixin:
    def falar(self):
        return "Estou falando"
    
    
class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

""" class Ornitorrinco(Mamifero, Ave):
    pass """
    
class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self,cor_bico,cor_pelo,patas):
        #print(Ornitorrinco.__mro__) #busca a ordem de execução dos metodos
        #print(super())
        super().__init__(cor_pelo=cor_pelo,cor_bico=cor_bico,patas=patas) # o super chama o metodo da classe pai
        
    def __str__(self):
        return 'Ornitorrinco'


""" gato = Gato(cor_pelo="preto",patas=4)
print(gato)
 """

onito = Ornitorrinco(patas=4, cor_pelo="marrom", cor_bico="laranja")
print(onito)
onito.__str__()
print(onito.falar())