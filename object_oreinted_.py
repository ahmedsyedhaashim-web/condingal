class Fruit:
  # constructor function - used for creating properties on the objects 
  def __init__(self, n, c, t, s):
    self.name = n
    self.color = c
    self.taste = t
    self.size = s

  # methods
  def info(self):
    return f"name: {self.name} | color: {self.color} | taste: {self.taste} | size: {self.size}"

# create object using the class
fruit1 = Fruit("Apple", "Red", "Sweet", "round")
fruit2 = Fruit("Orange", "Orange", "Sour", "round")
fruit3 = Fruit("Watermelon", "Green", "Sweet", "Oval")

print(fruit1)

# access the properties
print(fruit1.name)
print(fruit1.color)
print(fruit1.taste)
print(fruit1.size)

print(fruit2.name)
print(fruit2.color)
print(fruit2.taste)
print(fruit2.size)

print(fruit3.name)
print(fruit3.color)
print(fruit3.taste)
print(fruit3.size)

# access the method
print(fruit1.info())
print(fruit2.info())
print(fruit3.info())