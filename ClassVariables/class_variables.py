class Person:
    species = "Homo Species" # class variables.
    instance_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.instance_count += 1 # whenever a instance object's create, it will increment by 1.

    def display(self):
        print(f"{self.name} is {self.age} years old.")


p1 = Person("Mirza", 26)
p2 = Person("Mofeez", 25)

print(Person.species) # you can directly call Class variable without instance object.