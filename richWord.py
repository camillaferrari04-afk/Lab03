class RichWord:
    def __init__(self, parola:str):
        self._parola = parola # this is a string
        self._corretta = None #this is a bool

    @property
    def corretta(self) ->bool:
        # print("getter of parola called" )
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue:bool):
        # print("setter of parola called" )
        self._corretta = boolValue

    def __str__(self) ->str:
        return self._parola