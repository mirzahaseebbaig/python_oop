class MyClass():
    a = 5

    def __init__(self, x):
        self._x = x

    def method1(self):
        print(self.x)

    @classmethod
    def modthod2(cls):
        print(cls.a)


MyClass.modthod2()