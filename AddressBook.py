import Book

class AdressBook(Book):
    
    """Address Book"""
    def __init__(self, title, authors, legibility):
        super().__init__(title, authors)
        self._addresses = []
        self._legibilty = False
    
    #get
    
    @property
    def legibilty(self):
        return self._legibilty
    
    @property
    def addresses(self):
        return self._addresses
    #set


    @legibilty.setter
    def legibilty(self, new_legibilty):
        self._legibilty = new_legibilty
    
    @addresses.setter
    def addresses(self, new_addresses):
        self._addresses = new_addresses


    #func
    def read(self):
        print("Why is your handwriting like this? Who raised you?")
    
    def add_entry(self, entry):
        self.addresses.append(entry)