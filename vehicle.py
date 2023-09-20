class Vehicle:
    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def is_eco_friendly(self):
        if self.fuel == "gas":
            return False
        else:
            return True


class Car(Vehicle):
    def __init__(self, make, model, fuel="gas", num_wheel=4):
        super().__init__(make, model, fuel)
        self.numb_wheels = num_wheel


new_vehicle = Vehicle("zoom", "goes fast", fuel="cooking oil")
print(new_vehicle.fuel)
my_suburu = Car("Subaru", "Cross Trek", fuel="diesel")
print(my_suburu.fuel)
print(my_suburu.is_eco_friendly())
