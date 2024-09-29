class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("começou aqui")
        self.nome = nome
        self.cor =cor
        self.acordado=acordado
        
    def latir(self):
        print("auau")
        
    def __del__(self):
        print("removendo")
        
        
dog = Cachorro("bibi", "roxo")
dog.latir()
#dog.__del__()
del dog
print("maria")
#del dog