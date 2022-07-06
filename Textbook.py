import Book

class Textbook(Book):
    
    """Text Book"""
    def __init__(self, title, authors, genre, shape):
        super().__init__(title, authors, genre)
        self._shape = shape
        self._courserelevant = False
    
    #get

    @property
    def shape(self):
        return self._shape
    
    @property
    def courserelevant(self):
        return self._courserelevant
    
    #set

    @shape.setter
    def shape(self, new_shape):
        self._shape = new_shape

    @courserelevant.setter
    def courserelevant(self, new_courserelevant):
        self._courserelevant = new_courserelevant

    #func
    def sell_back(self):
        print("I paid 10x that for this. Fine. Whatever.")
        del self