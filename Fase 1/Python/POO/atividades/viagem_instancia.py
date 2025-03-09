from viagem import Viagem

viagem = Viagem()

viagem.opcoes_de_destino('São Paulo')
viagem.opcoes_de_destino('Rio de Janeiro')
viagem.opcoes_de_destino('Bahia')
viagem.opcoes_de_destino('Fortaleza')
viagem.opcoes_de_destino('Recife')

print('Digite seu nome: ')
nome = input()
print(f'Olá {nome}, escolha seu destino: ')
viagem.mostrar_opcoes()
destino = int(input())
print(f'Você escolheu {viagem.destino[destino - 1]} como destino da sua viagem') 