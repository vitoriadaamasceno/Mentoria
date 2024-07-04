class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo # esta protegido por convenção com o _ (underline)
        
    def sacar(self,valor):
        self._saldo -= valor
        return self._saldo
    
    def depositar(self,valor):
        self._saldo += valor
        return self._saldo
    
    def get_saldo(self):
        return self._saldo
    
conta = Conta(saldo=1000)

print(conta._saldo) #não é recomendado acessar o atributo diretamente

conta.depositar(1000)
print(conta.get_saldo())

#decorador é uma funcao que executa antes de outra funcao