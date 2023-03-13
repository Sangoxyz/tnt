class Car:

    wheels = 4      #class variable

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This " +self.model + "is driving")

    def stop(seft):
        print("This " +seft.model + "is stopped")