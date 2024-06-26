class Veiculo:
    def __init__(self, cor , placa, numero_rodas):
        self.cor = cor
        self.placa = placa 
        self.numero_rodas= numero_rodas
        
    def ligar(self):
        print(f"ligando...,{self.__class__.__name__}")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}:{valor}' for chave, valor in self.__dict__.items()])}"    
    

class Moto(Veiculo):
    pass

class Carro(Veiculo):
    def __init__(self, cor, placa, numero_rodas,carregado=False): #sobrescrevendo o metodo __init__ da classe
        super().__init__(cor, placa, numero_rodas) #chamando o metodo __init__ da classe pai
        self.carregado = carregado
    
    def combustivel(self):
        print(f"Carro {'não está' if not self.carregado else 'está'} carregado")   


motinha = Moto("azul", placa=8985, numero_rodas=2)
print(motinha)
motinha.ligar()

carro = Carro("vermelho", placa=1234, numero_rodas=4, carregado=True)
print(carro)
carro.ligar()
carro.combustivel()