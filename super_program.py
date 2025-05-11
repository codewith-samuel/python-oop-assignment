# Base class for superheroes
class Superhero:
    def __init__(self, name, power_level, secret_identity):
        self.name = name
        self.power_level = power_level
        self.__secret_identity = secret_identity  # Private attribute (encapsulation)
    
    def use_power(self):
        return f"{self.name} unleashes their power at level {self.power_level}!"
    
    def reveal_identity(self):
        return f"{self.name}'s secret identity is {self.__secret_identity}."
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move() method.")
    
    def increase_power(self, amount):
        self.power_level += amount
        return f"{self.name}'s power level increased to {self.power_level}."

# Subclass for flying superheroes
class FlyingHero(Superhero):
    def __init__(self, name, power_level, secret_identity, flight_speed):
        super().__init__(name, power_level, secret_identity)
        self.flight_speed = flight_speed
    
    def move(self):
        return f"{self.name} is flying at {self.flight_speed} mph! ✈️"
    
    def use_power(self):
        return f"{self.name} soars into the sky with a power level of {self.power_level}!"

# Subclass for speedster superheroes
class Speedster(Superhero):
    def __init__(self, name, power_level, secret_identity, run_speed):
        super().__init__(name, power_level, secret_identity)
        self.run_speed = run_speed
    
    def move(self):
        return f"{self.name} is running at {self.run_speed} mph! 🏃"
    
    def use_power(self):
        return f"{self.name} dashes with a power level of {self.power_level}!"

# Main program to demonstrate the classes
def main():
    # Create instances of superheroes
    superman = FlyingHero("Superman", 90, "Clark Kent", 1000)
    flash = Speedster("The Flash", 85, "Barry Allen", 750)
    
    # Demonstrate polymorphism with move()
    heroes = [superman, flash]
    print("=== Superhero Movements ===")
    for hero in heroes:
        print(hero.move())
    
    # Demonstrate other methods
    print("\n=== Superhero Actions ===")
    print(superman.use_power())
    print(flash.use_power())
    
    # Increase power level
    print("\n=== Power Boost ===")
    print(superman.increase_power(10))
    print(flash.increase_power(5))
    
    # Reveal secret identities (encapsulation)
    print("\n=== Secret Identities ===")
    print(superman.reveal_identity())
    print(flash.reveal_identity())

if __name__ == "__main__":
    main()