from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def liga(self):
        pass
    
    @abstractmethod
    def desliga(self):
        pass

class ControleTV(ControleRemoto):
    def liga(self):
        print("Ligando a TV")
    
    def desliga(self):
        print("Desligando a TV")
        
class ControleRadio(ControleRemoto):
    def liga(self):
        print("Ligando o Radio")
    
    def desliga(self):
        print("Desligando o Radio")
        
        
tv = ControleTV()
tv.liga()
tv.desliga()
radio = ControleRadio()
radio.liga()
radio.desliga()

#controle = ControleRemoto() #não é possivel instanciar uma classe abstrata