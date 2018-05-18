class Vehicle:
    def __init__(self):
        raise NotImplementedError('Do no make raw Vehicle objects.')

    def __str__(self):
        return self.name

class Motorcycle(Vehicle):
    def __init__(self):
        self.name = 'Motorcycle'
        self.wheels = 2

class Car(Vehicle):
    def __init__(self):
        self.name = 'Car'
        self.wheels = 4

print(Motorcycle())
print(Motorcycle().wheels)
print(Car())
print(Car().wheels)
print(Vehicle())
