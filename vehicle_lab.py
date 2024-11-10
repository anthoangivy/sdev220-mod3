# Name: Anthony Hoang
# File: vehicle_lab.py
# Description: This program will ask the user to input their vehicle's type, year, make, model, number of doors, and roof style. It will then output the information in a readable format.

class Vehicle:
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def info(self):
        print(f"Vehicle type: {self.type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Roof style: {self.roof}")

def details():
    type = input("Vehicle type: ")
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Number of doors: ")
    roof = input("Roof style: ")

    car = Automobile(type, year, make, model, doors, roof)
    car.info()

details()