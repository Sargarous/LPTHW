class Car(object):
    def __init__(self, brand, model, body, max_speed):
        self.brand = brand
        self.model = model
        self.body = body
        self.max_speed = max_speed

    def car_description(self):
        print(f"This is {self.model}, {self.brand} in '{self.body}' body, can reach {self.max_speed} km/h")

class Acceleration(object):
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def accel(self):
        print("Acceleration is " + str(self.max_speed/20) + " sec from 0 to 100 km.")

class SportCar(Car):

    def __init__(self, brand, model, body, max_speed):
        super().__init__(brand, model, body, max_speed)
        self.acceler = Acceleration(190)

car_desc = SportCar('BMW', 'E39', 'saloon', 194)
car_desc.car_description()
car_desc.acceler.accel()
