'''
Antes de começar vamos entender o que são classes e o uso de funções em Python.
classes são estruturas que representam objetos, ou seja, são modelos que definem os atributos e métodos que um objeto deve ter.
Funções são blocos de código que executam uma determinada tarefa.
'''
class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """
    
time = Time()
time.hora = 1
time.minuto = 20
time.segundo = 25


    
time2 = Time()
time2.hora = 9
time2.minuto = 10
time2.segundo = 30

def print_time(time):
    print("{:2d}:{:2d}:{:2d}".format(time.hora, time.minuto, time.segundo))

#print(print_time(time))

#Escreva uma função booleana chamada is_after, que receba dois objetos Time, t1 e t2, e devolva True se t1 for cronologicamente depois de t2 e False se não for. Desafio: não use uma instrução if.

def is_after(t1,t2):
    return (t1.hora, t1.minuto, t1.segundo) > (t2.hora, t2.minuto , t2.segundo)

#print(is_after(time, time2))


def add_time(t1, t2):
    sum = Time()
    sum.hora = t1.hora + t2.hora
    sum.minuto = t1.minuto + t2.minuto
    sum.segundo = t1.segundo + t2.segundo
    print_time(sum)
    return sum

add_time(time, time2)
