from Animal import Animal


class Fish(Animal):

    def __init__(self, species, birthdate, watersalinity):
        super().__init__(species, birthdate)
        self._watersalinity = watersalinity
    
    #set
    @property
    def watersalinity(self):
        return self._watersalinity
    
    #get
    @watersalinity.setter
    def watersalinity(self, new_watersalinity):
        self._watersalinity = new_watersalinity

    #func
    def swim(self, new_loc):
        print("Just keep swimming")
        super().move(new_loc)