# in this Person class you we are using validation twice, which is not good practice for private variables,
# please check property_deep_1.py File.

class Person:
    def __init__(self, name, age):
        self.name = name
        if 20 < age < 80: # if age greater than 20 and less than 80.
            self._age = age
        else:
            raise ValueError('Age must be between 20 and 80')

    def display(self):
        print(self.name, self._age)

    def set_age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age # _age is private variable.
        else:
            raise ValueError('Age must be between 20 and 80')

    def get_age(self):
        return self._age


p1 = Person("Mirza", 26)

print(p1.get_age())