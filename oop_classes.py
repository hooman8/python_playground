int(5)
type(int(5))


class Car:
    runs = True

    def __init__(self, name):
        self.name = name
        print(f"Does run? {self.runs}")

    def start(self):
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken")


my_car = Car("Sabura")
my_car.start()

# inside of the reple
# from oop_classes import Car

# import oop_classes
# import importlib
# importlib.reload(oop_classes)
# type(oop_classes.Car)
