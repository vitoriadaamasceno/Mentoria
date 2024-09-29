
class Bike:
    def __init__(self,cor, modelo,ano,valor,marcha=1):
        self.cor =cor
        self.modelo=modelo
        self.ano=ano
        self.valor=valor
        self.marcha = marcha
        
    def buzinar(self):
        print("Buzinando...")
        
    def parar(self):
        print("parando")
        
    def _trocar_marcha(self, n_marcha):
        if n_marcha > self.marcha:
            print("Marcha trocada")
        else:
            print("não foi possivel")

    def trocar_marcha(self, n_marcha):
        print("trocando")
        self._trocar_marcha(n_marcha)

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}:{valor}' for chave, valor in self.__dict__.items()])}"
        
        
bike1 = Bike("azul","grande", 2020,1200,1)
bike1.buzinar() # Bike.buzinar(bike1)
print(bike1.__str__())
bike1.trocar_marcha(0)