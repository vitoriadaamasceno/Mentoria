class Viagem:
    def __init__(self):
        self.destino = []

    def opcoes_de_destino(self, destino):
        self.destino.append(destino)

    def mostrar_opcoes(self):
        i = 0
        for destino in self.destino:
            i += 1
            print(f'{i} - {destino}')
