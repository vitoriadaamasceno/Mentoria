class Estudante:
    escola = 'Escola Estadual' #variável de classe
    def __init__(self, nome, matricula):
        self.nome = nome #variável de instância
        self.matricula = matricula

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.matricula}, Escola: {self.escola}'
    
    
aluno1 = Estudante('João', 123)
aluno2 = Estudante('Maria', 456)
print(aluno1)
print(aluno2)


aluno1.matricula = 999
print(aluno1)
Estudante.escola = 'Escola Municipal' #alterando a variável de classe
aluno_3 = Estudante('José', 789)
print(aluno1)
print(aluno2)
print(aluno_3)
Estudante.nome = "todes" #nao é possivel alterar a variável de instância dessa forma
print(aluno1)
#atributos de classe são compartilhados entre todas as instâncias da classe
#atributos de instância são específicos de cada instância da classe