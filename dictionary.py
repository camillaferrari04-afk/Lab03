class Dictionary:
    def __init__(self):
        self._dict=[]

    def loadDictionary(self,path):
        try:
            infile = open(path,"r")
            for line in infile:
                self._dict.append(line.strip())
            infile.close()
        except FileNotFoundError:
            print("Documento non trovato")
            pass

    def printAll(self):
        return self._dict

    @property
    def dict(self):
        return self._dict