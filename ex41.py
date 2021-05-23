class Dog(object):
    def __init__(self, breed, age, weight, bark, speed):
        self.breed = breed
        self.age = age
        self.weight = weight
        self.bark = bark
        self.speed = speed

    def speak(self):
        print(f"I am {self.breed}, {self.age} years old, {self.weight} weight, {self.bark}, i can run at {self.speed}")

mastif = Dog('mastif', 2, 35, 'woof-woof', 26)
mastif.speak()

dog_hound = Dog('dog hound', 8, 15, 'uff', 23)
dog_hound.speak()
