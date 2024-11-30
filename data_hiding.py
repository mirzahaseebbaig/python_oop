class Product:
    def __init__(self):
        self.data1 = 10
        self._data2 = 20 #programer should respect that variable which starts with _ underscore in python and don't change.

    def methodA(self):
        pass

    def _methodB(self): #programer should respect that method which starts with _ underscore in python and don't change.
        pass


p = Product()