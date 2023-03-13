# prevents a user from creating an ojbect of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract methods = a methods tha has a declaration but does not have an implementation

from abc import ABC, abstractmethod

class Vehicle:

    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")
    def stop(self):
        print("You car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("You motorcycle is stopped")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()
