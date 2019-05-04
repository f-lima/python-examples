class Animal:
    def __init__(self, species = None):
        self._species = species

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        self._species = value

class DomesticAnimal(Animal):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

class Human(Animal):
    def __init__(self):
        super().__init__('Human')

class Person(Human):
    __count = 0

    @property
    def count(self):
        return Person.__count

    @count.setter
    def count(self, value):
        Person.__count = value

    def __init__(self, name):
        super().__init__()
        self._name = name
        Person.__count += 1
        print(f"{self.count} citizens:   {self.name} was born")

    def __del__(self):
        Person.__count -= 1
        print(f"{self.count} citizens:   {self.name} died")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

john = Person("John Doe")
mary = Person("Mary Doe")
del mary

print('')
print(f"Person is subclass of Animal? {issubclass(Person, Animal)}")
print(f"Person is subclass of DomesticAnimal? {issubclass(Person, DomesticAnimal)}")
print(f"Animal is subclass of Person? {issubclass(Animal, Person)}")
print(f"Animal is subclass of DomesticAnimal? {issubclass(Animal, DomesticAnimal)}")
print(f"DomesticAnimal is subclass of Person? {issubclass(DomesticAnimal, Person)}")
print(f"DomesticAnimal is subclass of Animal? {issubclass(DomesticAnimal, Animal)}")
print('')
print(f"{john.name} is instance of Person? {isinstance(john, Person)}")
print(f"{john.name} is instance of Human? {isinstance(john, Human)}")
print(f"{john.name} is instance of Animal? {isinstance(john, Animal)}")
print(f"{john.name} is instance of DomesticAnimal? {isinstance(john, DomesticAnimal)}")
print('')
print(f"{john.name} is a {john.__class__.__name__}.")
print(f"{john.name} is a {john.species}.")
print('')

# [Running] python -u "d:\dev\test\python\inheritance.py"
# 1 citizens:   John Doe was born
# 2 citizens:   Mary Doe was born
# 1 citizens:   Mary Doe died

# Person is subclass of Animal? True
# Person is subclass of DomesticAnimal? False
# Animal is subclass of Person? False
# Animal is subclass of DomesticAnimal? False
# DomesticAnimal is subclass of Person? False
# DomesticAnimal is subclass of Animal? True

# John Doe is instance of Person? True
# John Doe is instance of Human? True
# John Doe is instance of Animal? True
# John Doe is instance of DomesticAnimal? False

# John Doe is a Person.
# John Doe is a Human.

# 0 citizens:   John Doe died
# [Done] exited with code=0 in 0.137 seconds

""" Shows how to: 
1. create a derived class from a base class
2. call a method in a base class (using super)
3. verify if a class is derived from another class (using issubclass)
4. verify if an object is based on a class or any of its derived class (using isinstance)
5. create a instance counter that returns the number of objects actives in memory (property count)
6. increment and decrement automatically the instance counter (using __init__ and __del__)
7. log when a new object is created and when it is removed from memory (using __init__ and __del__)
8. remove intentionally an object from memory (using del)
9. create a method or constructor with optional parameters (Animal.__init__)
10. overwrite a method defined in a base class (Human.__init__)
11. gets the class name of an object (using __class__.__name__)
 """
