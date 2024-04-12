def is_triangle(a, b, c ):
    if a > b+c or b>a+c or c>b+a:
        print('NO')
    else :
        print('YES')

is_triangle(10,10,21)