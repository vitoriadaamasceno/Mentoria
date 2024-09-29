
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
    def abrir_conta(self, conta):
        self.contas.append(conta)
        
    def realizar_transacoes(self, conta, transacao):
        transacao.registrar(conta)
    
class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        
class Conta:
    def __init__(self,numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()
        
    