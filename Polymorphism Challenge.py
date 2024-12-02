# Base Class: Vehicle
class Vehicle:
    def move(self):
        pass  # This will be overridden in subclasses

# Subclass: Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Example Usage
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
