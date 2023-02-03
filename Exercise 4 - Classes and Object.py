class Animal:
    def __init__(self, legs_count):
        print("Animal object was created")
        self._number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self._number_of_legs}")

    def return_legs(self):
        return self._number_of_legs


animal = Animal(4)
animal.count_legs()
print(animal.return_legs())
print(animal._number_of_legs)

class Dog(Animal):
    def __int__(self,name):
        self.__name=name


    def name_of_dog(self):
        print("Dog's name is",self.__name)
    def bark(self):
        print("woof woof")

newDog = Dog("yuceltan")
newDog.name_of_dog()
newDog.bark()


