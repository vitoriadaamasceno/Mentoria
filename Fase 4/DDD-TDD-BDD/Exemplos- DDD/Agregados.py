class  Order : 
    '''Classe que representa um pedido, seria um agregado pois une uma entidade (Pedido) com um ou mais objetos de valor que é o PedidoItem.
    '''
    def  __init__ ( self, id : int , line_items: List [LineItem] ):  # type: ignore
        self. id = id
        self.line_items = line_items 

    def  process ( self ): 
        # processa o pedido 
        pass