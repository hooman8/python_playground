class Car:
    runs = True

    def start(self):
        if self.runs:
            print("Car is started.")
        else:
            print("Car is broken.")


my_car = Car()
my_car.runs = False
my_car.start()

print(isinstance(my_car, Car))
