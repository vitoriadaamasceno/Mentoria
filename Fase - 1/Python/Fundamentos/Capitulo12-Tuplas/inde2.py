#args é uma tupla, que recebe os valores passados para a função
def world_cup_titles(country, *args):
    print('Country: ', country)
    for title in args:
        print('year: ', title)
    print(args)
        
world_cup_titles('Brazil', 1958, 1962, 1970, 1994, 1994)

#kwargs é um dicionário, que recebe os valores passados para a função
def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    print(kwargs)
    return value


print(calculate_price(100.0, tax_percentage=7, discount=5.0))