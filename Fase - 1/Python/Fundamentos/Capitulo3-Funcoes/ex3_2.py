#1


def right_justify(sim):
    print(" "*70 + sim)

right_justify("amor")

def print_spam(valor):
    print(valor)
    print(valor)

def do_twice(f,s=None):
    f()
    f()
    if s is not None:
        print(s)


def  do_four(funcao, valor):
    funcao(valor)
    funcao(valor)

valor="maria"
do_four(print_spam,valor)