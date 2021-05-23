## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a object of Animal class
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a object of Animal class
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a object of Preson class
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a name
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    def __init__(self, breed, speed):
        self.breed = breed
        self.speed = speed

    def swim(self):
        print(f"{self.breed} swim speed is {self.speed} m/sec")

class Fish_jump():
    def __init__(self, height = 0):
        self.height = height

    def jump(self, height):
        print(f" and jump in {self.height} height")

## Salmon is-a object os Fish class
class Salmon(Fish):
    def __init__(self, breed, speed):
        super().__init__(breed, speed)
        self.jump_up = Fish_jump()

salmon_description = Salmon('Salmon', 15)
salmon_description.swim()
salmon_description.jump_up.jump(44)



## Halibut os-a object of Fish class
class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a satan pet
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish('Flipper', 12)
flipper.swim()
## crouse is-a Salmon
crouse = Salmon('Crouse', 99)
crouse.swim()
## harry is-a Halibut
harry = Halibut('Harry', 10)
harry.swim()
