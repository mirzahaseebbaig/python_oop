class Product:
    def __init__(self):
        self.data1 = 10
        self._data2 = 20 #programer should respect that variable which starts with _ underscore in python and don't change.
        self.__data3 = 30 #you can not directly call this.

    def methodA(self):
        pass

    def _methodB(self): #programer should respect that method which starts with _ underscore in python and don't change.
        pass

    def __methodC(self): #you can not directly call this method.
        pass


p = Product()

# p.__methodC() it will throw error, use dir(p) to see the hidden name and call via that name. ex -> _Product__methodC()
p._Product__methodC()