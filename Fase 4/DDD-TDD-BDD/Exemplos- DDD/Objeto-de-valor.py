import datetime


class ProductReview:
    ''' 
    Objeto de valor que representa uma avaliação de um produto, pois não tem identidade própria mas é parte de um produto. 
    '''
    def __init__(self, rating: int, text: str, posted_date: datetime):
        self.rating = rating
        self.text = text
        self.posted_date = posted_date