class Pessoa:
    def __init__(self,nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        
    #para nao criar duas instacias de uma mesma classe, podemos criar um metodo de classe
    @classmethod
    def criar_apartir_data_nascimento(cls, nome, ano):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod #metodo estatico é um metodo que nao precisa de uma instancia da classe
    def maior_de_idade(idade):
        return idade >= 18
    
""" pessoa = Pessoa("Maria", 25)
print(pessoa.nome)
print(pessoa.idade) """
""" pessoa2 = Pessoa.criar_apartir_data_nascimento("João", 1999)
print(pessoa2.nome)
print(pessoa2.idade)

 """

print(Pessoa.maior_de_idade(25)) #nao precisa de uma instancia da classe
print(Pessoa.maior_de_idade(15))