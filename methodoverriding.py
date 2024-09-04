# Base class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return f"{self.make} {self.model} engine started."

    def __str__(self):
        return f"Vehicle: {self.make} {self.model}"

# Derived class
class ElectricCar(Vehicle):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)  # Call the initializer of the base class
        self.battery_capacity = battery_capacity

    def start_engine(self):
        # Overriding the start_engine method
        return f"{self.make} {self.model} engine started silently."

    def charge_battery(self):
        return f"Charging battery of {self.make} {self.model} with capacity {self.battery_capacity} kWh."

    def __str__(self):
        return f"Electric Car: {self.make} {self.model}, Battery Capacity: {self.battery_capacity} kWh"

# Another derived class
class GasCar(Vehicle):
    def __init__(self, make, model, fuel_tank_capacity):
        super().__init__(make, model)  # Call the initializer of the base class
        self.fuel_tank_capacity = fuel_tank_capacity

    def start_engine(self):
        # Overriding the start_engine method
        return f"{self.make} {self.model} engine roars to life."

    def refuel(self):
        return f"Refueling {self.make} {self.model} with fuel capacity {self.fuel_tank_capacity} liters."

    def __str__(self):
        return f"Gas Car: {self.make} {self.model}, Fuel Tank Capacity: {self.fuel_tank_capacity} liters"

# Creating instances of ElectricCar and GasCar
electric_car = ElectricCar(make="Tesla", model="Model S", battery_capacity=100)
gas_car = GasCar(make="Toyota", model="Corolla", fuel_tank_capacity=50)

# Using the instances
print(electric_car)              # Output: Electric Car: Tesla Model S, Battery Capacity: 100 kWh
print(electric_car.start_engine())  # Output: Tesla Model S engine started silently.
print(electric_car.charge_battery())  # Output: Charging battery of Tesla Model S with capacity 100 kWh.

print(gas_car)                   # Output: Gas Car: Toyota Corolla, Fuel Tank Capacity: 50 liters
print(gas_car.start_engine())   # Output: Toyota Corolla engine roars to life.
print(gas_car.refuel())         # Output: Refueling Toyota Corolla with fuel capacity 50 liters.
