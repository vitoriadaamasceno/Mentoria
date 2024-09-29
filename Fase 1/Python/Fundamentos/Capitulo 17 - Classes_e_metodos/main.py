'''
Antes de começar vamos entender o que são classes ,métodos e funções em Python.

Classes são estruturas que representam objetos, ou seja, são modelos que definem os atributos e métodos que um objeto deve ter.
Funções são blocos de código que executam uma determinada tarefa.
Métodos são funções que pertencem a uma classe.
'''

class Time:
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
        
#metodo init é um método especial que é executado quando um objeto é instanciado.
class Times:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second