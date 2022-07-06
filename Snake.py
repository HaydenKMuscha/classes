import Animal

class Snake(Animal):
    
    """Snake"""
    
    def __init__(self, species, terrain, killtype):
        super().__init__(species)
        self.__terrain = terrain
        self.__killtype = killtype

    #get    
    @property
    def terrain(self):
        return self.__terrain
    
    @property
    def killtype(self):
        return self.__killtype
    
    #set
    @terrain.setter
    def species(self, new_terrain):
        self.__terrain = new_terrain
    
    @killtype.setter
    def species(self, new_killtype):
        self.__killtype = new_killtype
    
    #func
    def slide(self, new_loc):
        print('*Hisss* I am gonna slide my way to the rat buffet')
        super().move(new_loc)