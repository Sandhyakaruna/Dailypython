# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def __str__(self):
        return f"Animal: {self.name}"

# Subclass
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the base class
        self.breed = breed

    def speak(self):
        return "Woof!"

    def __str__(self):
        return f"Dog: {self.name}, Breed: {self.breed}"

# Another subclass
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call the constructor of the base class
        self.color = color

    def speak(self):
        return "Meow!"

    def __str__(self):
        return f"Cat: {self.name}, Color: {self.color}"

# Creating instances of Dog and Cat
dog = Dog(name="Rex", breed="German Shepherd")
cat = Cat(name="Whiskers", color="Gray")

# Using the instances
print(dog)           # Output: Dog: Rex, Breed: German Shepherd
print(dog.speak())  # Output: Woof!

print(cat)           # Output: Cat: Whiskers, Color: Gray
print(cat.speak())  # Output: Meow!
