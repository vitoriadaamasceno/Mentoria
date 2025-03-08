class  ProductSearchService : 
    '''
    Suponha que você precise implementar um recurso de pesquisa de produtos na plataforma de e-commerce. 
    Você pode criar uma ProductSearchServiceclasse que tenha um search() método que pegue um conjunto de critérios de pesquisa 
    e retorne uma lista de produtos que correspondam a esses critérios. 
    '''
    def  __init__ ( self, products: List [Product] ): # type: ignore
        self.products = products 

    def  search ( self, criterio: str ) -> List [Product]: # type: ignore
        # pesquisa os produtos com base nos critérios fornecidos 
        pass