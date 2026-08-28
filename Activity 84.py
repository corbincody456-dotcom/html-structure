class Vehicle:

  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"Brand: {self.brand}")
    print(f"Model: {self.model}")
    print(f"Year: {self.year}")


class Car(Vehicle):

  def __init__(self, brand, model, year, doors):
    super().__init__(brand, model, year)
    self.doors = doors

  def display_info(self):
    super().display_info()
    print(f"Doors: {self.doors}")


class Motorcycle(Vehicle):

  def __init__(self, brand, model, year, has_carrier):
    super().__init__(brand, model, year)
    self.has_carrier = has_carrier

  def display_info(self):
    super().display_info()
    print(f"Has Carrier: {'Yes' if self.has_carrier else 'No'}")


def main():
  print("Vehicle Builder")
  print("1. Car")
  print("2. Motorcycle")

  choice = input("Select vehicle type (1 or 2): ")
  brand = input("Enter brand: ")
  model = input("Enter model: ")
  year = input("Enter year: ")

  if choice == "1":
    doors = input("Enter number of doors: ")
    vehicle = Car(brand, model, year, doors)
  elif choice == "2":
    carrier = input("Does it have a carrier? (y/n): ").lower() == "y"
    vehicle = Motorcycle(brand, model, year, carrier)
  else:
    print("Invalid choice.")
    return

  print("\n--- Your Vehicle ---")
  vehicle.display_info()


if __name__ == "__main__":
  main()