# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass

# Put a comment noting which class is the base class
# Vechile is the base class
class Vehicle:
    def __init__(self,name,groundVehicle=[],flightVehicle=[]):
        self.name = name
        self.groundVehicle = groundVehicle
        self.flightVehicle = flightVehicle

class GroundVehicle:
    def __init__(self,type):
        self.type
    
    def __str__(self):
        return (f"{self.type}")

class Car(GroundVehicle):
    def __init__(self, name, mileage, type):
        super().__init__(name)
        self.name
        self.mileage

    def __str__(self):
        return (f"{self.name}, {self.mileage}, {self.type}")

class Motorcycle(GroundVehicle):
    def __init__(self, name, mileage, type):
        super().__init__(name)
        self.name
        self.mileage

    def __str__(self):
        return (f"{self.name}, {self.mileage}, {self.type}")

class FlightVehicle:
    def __init__(self,type):
        self.type
    
    def __str__(self):
        return (f"{self.type}")

class Airplane(FlightVehicle):
    def __init__(self, name, type):
        super().__init__(name)
        self.name
       

    def __str__(self):
        return (f"{self.name}, {self.type}")

class StarShip(FlightVehicle):
    def __init__(self, name, type):
        super().__init__(name)
        self.name
        

    def __str__(self):
        return (f"{self.name}, {self.type}")