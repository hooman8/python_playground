class Vehicle:
    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def __str__(self):
        return f"I drive {self.make} {self.model}. It runs on {self.fuel}."


class Car(Vehicle):
    number_of_wheels = 4


class Truck(Vehicle):
    number_of_wheels = 6

    def __init__(self, make, model, fuel="diesel"):
        super().__init__(make, model, fuel)


daily = Vehicle("Subaru", "Crosstrek")
print(f"I drive {daily.make} {daily.model}. It runs on {daily.fuel}.")
print(f" for class: {Vehicle.number_of_wheels}")
print(f" for instance: {daily.number_of_wheels}")
