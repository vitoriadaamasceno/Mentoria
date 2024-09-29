# mesmo metodos com nomes iguais, mas com comportamentos diferentes
class Passaro:
        
    def voar(self):
        print("Voando...")
    
class Pardal(Passaro):
    def voar(self):
      return super().voar()
        
class Pinguim(Passaro):
    def voar(self):
        print("Pinguim não voa")
        
def voar_como_um_passaro(passaro):
    passaro.voar()
    
pardal = Pardal()
pinguim = Pinguim()
voar_como_um_passaro(pardal)
voar_como_um_passaro(pinguim)