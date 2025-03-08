class  Product : 
    '''
    Uma Productclasse que tenha propriedades como id, name, description, price, e availability,
    e métodos como add_to_cart()e remove_from_cart(). Ele seria uma entidade, pois tem uma identidade própria e é distinto de outros objetos.
    '''
    def  __init__ ( self, id : int , name: str , description: str , price: float , availability: bool ): 
        self. id = id
        self.name = name
        self.description = description
        self.price = price
        self.availability = availability 

    def  add_to_cart ( self ): 
        # adiciona o produto ao carrinho de compras do usuário 
        pass 

    def  remove_from_cart ( self ): 
        # remove o produto do carrinho de compras do usuário 
        pass