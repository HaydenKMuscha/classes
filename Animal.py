class Animal:

    """Animal"""

    def __init__(self, species, birthdate):
        self._species = species
        self._birthdate = None
    
    #Get

    @property
    def species(self):
        return self._species
    
    @property
    def birthdate(self):
        return self._birthdate

    #set

    @species.setter
    def species(self, new_species):
        self._species = new_species

    @birthdate.setter
    def birthdate(self, new_birthdate):
        self._birthdate = new_birthdate
    
    #function

    def move(self):
        print('Moving')

    def eat():
        print('omnomnom')

    def reproduce():
        print("*Sims Voice*: Woohoo")
