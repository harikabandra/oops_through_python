class vehicle:
    def display_details(self):
        print("Brand : BMW")
        print("Model : Innova")
        

class car(vehicle):
    def car_details(self):
        print("Type : car")
        

class bike(vehicle):
    def bike_details(self):
        print("Type : bike")
        

car = car()
bike = bike()

print("car_details")
car.display_details()
car.car_details()

print("bike_details")
bike.display_details()
bike.bike_details()