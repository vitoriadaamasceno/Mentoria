quantidade_de_saque=0
saldo =0
limite=500
numeros_de_saque=0
extrato_saque = []
extrato_deposito=[]
LIMITE_DE_SAQUE=3

#Deposito
def deposito(valor):
  global saldo
  global extrato_deposito
  if valor>0:
    saldo=saldo+valor
    extrato_deposito.append(valor)
    print('Valor depositado, seu saldo atual é:',saldo)
  else:
    print('Valor deve ser maior que 0')

def saque(valor):
  global saldo
  global extrato_saque
  global quantidade_de_saque
  quantidade_de_saque += 1
  if quantidade_de_saque<=LIMITE_DE_SAQUE:
    if valor<=limite:
      if valor<=saldo:
        saldo=saldo-valor
        extrato_saque.append(valor)
        print('Valor sacado, seu saldo atual é:',saldo)
      else:
        print('Você não tem saldo suficiente')
    else:
      print('Valor a acima do limite por saque')
  else:
    print('Limite de saque excedido, permitido apenas 3 saques por dia')

def extrato(): 
  global extrato_saque
  global extrato_deposito
  global saldo
  print('Extrato de depositos:', extrato_deposito)
  print('Extrato de saques:', extrato_saque)
  print('Saldo atual:', saldo)

while True:
  opcao = input('Digite a opção desejada: 1-Deposito, 2-Saque, 3-Extrato, 4-Sair: ')
  
  if opcao == '1':
    valor=float(input('Digite o valor do deposito: '))
    deposito(valor)
  
  elif opcao == '2':
    valor=float(input('Digite o valor do saque: '))
    saque(valor)

  elif opcao == '3':
    extrato()
    
  elif opcao == '4':
    print('Saindo...')
    break
  else:
    print('Opção inválida')
