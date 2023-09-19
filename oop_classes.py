# int(5)
# type(int(5))


class Car:
    runs = True
    number_of_wheels = 4

    def __init__(self, name):
        self.name = name
        # print(f"Does run? {self.runs}")

    def start(self):
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken")

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels


my_car = Car("Sabura")
my_car.get_number_of_wheels()
# my_car.start()
# inside of the reple
# from oop_classes import Car
print(isinstance(my_car, Car))
# import oop_classes
# import importlib
# importlib.reload(oop_classes)
# type(oop_classes.Car)


isinstance(True, int)  # booleans are subclass of int
# True + True <-- this gives you 2
issubclass(int, object)
