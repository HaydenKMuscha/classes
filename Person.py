import Animal

class Person(Animal):
    
    """Person"""
    
    def __init__(self, species, birthdate, name, diet):
        super().__init__(species, birthdate)
        self.__name = name
        self.__diet = diet

    #get    
    @property
    def name(self):
        return self.__name
    
    @property
    def diet(self):
        return self.__diet
    
    #set
    @name.setter
    def species(self, new_name):
        self.__name = new_name
    
    @diet.setter
    def species(self, new_diet):
        self.__diet = new_diet
    
    #func
    def walkin(self, new_loc):
        print("Ayyyyy, I'm walkin here!")
        super().move(new_loc)