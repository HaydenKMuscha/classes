class Vehicle:

    """Vehicle"""

    def __init__(self, make, model, transmission):
        self._make = make
        self._model = model
        self._transmission = transmission
        self._year = None
        self._mpg = None
        self._current_speed = 0
        self._running = False
    
    #Get

    @property
    def make(self):
        return self._make
    
    @property
    def model(self):
        return self._model
    
    @property
    def transmission(self):
        return self._transmission

    @property
    def year(self):
        return self._year
    
    @property
    def mpg(self):
        return self._mpg

    @property
    def current_speed(self):
        return self._current_speed

    @property
    def running(self):
        return self._running

    #set

    @make.setter
    def make(self, new_make):
        self._make = new_make

    @model.setter
    def model(self, new_model):
        self._model = new_model

    @transmission.setter
    def transmission(self, new_transmission):
        self._transmission = new_transmission
    
    @mpg.setter
    def mpg(self, new_mpg):
        self._mpg = new_mpg
    #function

    def accelerate(self, current_speed):
        self._current_speed +=1

    def brake(self, current_speed):
        self._current_speed -=1

    def enginestart(self, running):
        self._running = True

    def enginestop(self, running):
        self._running = False


