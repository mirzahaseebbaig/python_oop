class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('I am', self.name, self.age, 'years old.')

    @classmethod # @classmethod will return instance of the same class as well.
    def from_str(cls, s):
        name, age = s.split(',')
        return cls(name, int(age))

    @classmethod
    def from_dict(cls, d):
        return cls(d['name'], d['age'])

p1 = Person('Mirza', 26)
p2 = Person('Mofeez', 25)

s = "Jim, 23"
p3 = Person.from_str(s)
p3.display()

d = dict(name = 'Imran', age = 34)
p4 = Person.from_dict(d)
p4.display()
