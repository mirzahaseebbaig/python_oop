class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("I'm", self.name)

    def great(self):
        if self.age < 80:
            print("Hello, how are you doing?")
        else:
            print("Hi, How do you do? ")
        self.display()


p1 = Person("Mirza", 26)
p2 = Person()

p1.great()
