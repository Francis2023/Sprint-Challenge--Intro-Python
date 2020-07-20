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
class Vehicle:
    def __init__(self,name,groundVehicle=[],flightVehicle=()):
        self.name = name
        self.groundVehicle = groundVehicle
        self.flightVehicle = flightVehicle

class GroundVehicle:
    def __init__(self,name):
        self.name

class Car(GroundVehicle):
    def __init__(self, name, mileage):
        super().__init__(name)
        self.name

        
