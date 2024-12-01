class Product:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x, self._y)

    @property # this is getter method.
    def value(self): #by this @property keyword, you don't need to use () to call value ex-> obj.value, but you can't set value
        return self._x

    @value.setter # this is a setter method.
    def value(self, val): #with the help of this you can set value
        self._x = val