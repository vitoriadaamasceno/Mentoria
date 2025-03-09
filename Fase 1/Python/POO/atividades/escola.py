class Pessoa:
   def __init__(self, nome, data_nascimento, cpf):
      self.nome = nome
      self.data_nascimento = data_nascimento
      self.cpf = cpf


class Aluno(Pessoa):
    def __init__(self,nome, data_nascimento, cpf, matricula):
        super().__init__(nome, data_nascimento, cpf)
        self.matricula = matricula

class Professor(Pessoa):
    def __init__(self,nome, data_nascimento, cpf, displina):
        super().__init__(nome, data_nascimento, cpf)
        self.displina = displina

class Curso:
    def __init__(self, nome, carga_horaria, professor):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.professor = professor


