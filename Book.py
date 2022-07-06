class Book:

    """Book"""

    def __init__(self, title, authors, genre):
        self._title = title
        self._authors = authors
        self._genre = genre
        self._page_count = None
        self._year_published = None
        self._current_page = 1
    
    #Get

    @property
    def title(self):
        return self._title
    
    @property
    def authors(self):
        return self._authors
    
    @property
    def genre(self):
        return self._genre

    @property
    def page_count(self):
        return self._page_count
    
    @property
    def year_published(self):
        return self._year_published

    @property
    def current_page(self):
        return self._current_page

    #set

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @authors.setter
    def authors(self, new_authors):
        self._authors = new_authors

    
    #function

    def turnpage(self, page):
        self._current_page +=1

    def publish_book(self, date):
        self._year_published = date
