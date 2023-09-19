int(5)
type(int(5))


class Car:
    runs = True

    def __init__(self):
        print(f"Does run? {self.runs}")

    def start(self, name):
        self.name = name
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken")


# inside of the reple
# from oop_classes import Car

# import oop_classes
# import importlib
# importlib.reload(oop_classes)
# type(oop_classes.Car)
