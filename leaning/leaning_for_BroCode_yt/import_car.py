# car
""" from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "Red") """

""" print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color) """
""" 
car_1.drive()
car_2.stop() """

# method chaining = calling multiple methods seqentially
#                   each call performs an action on the same object and returns self

""" class Car:
    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()

car.turn_on().drive()

car.brake().turn_off()

car.turn_on().drive().brake().turn_off() """

class Car:

    color = None

class Motorcycle:
    color = None

def change_color(vehicle,color):

    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()
bike_1 = Motorcycle()

change_color(car_1, "Red")
change_color(car_2, "White")
change_color(car_3, "blue")
change_color(bike_1, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)

