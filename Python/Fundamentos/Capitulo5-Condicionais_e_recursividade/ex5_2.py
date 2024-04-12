

def check_fermant(a, b, c, n):
    if n <= 2:
        print("No, that doesn’t work.")
    else:
        if a**n + b**n == c**n :
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn’t work.")

check_fermant(2,2,10,1)


def check_fermant_user(a=input(), b=input(), c=input(), n=input()):
    aint = int(a)
    bint = int(b)
    cint = int(c)
    nint= int (n)
    if nint <= 2:
        print("No, that doesn’t work.")
    else:
        if aint**nint + bint**nint == cint**nint :
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn’t work.")

check_fermant_user()