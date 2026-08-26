# oops class inhertiance
# abstraction in python classes
from abc import ABC, abstractmethod

# parent or super or base class
class Person(ABC):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def info(self):
    return f"{self.name} and {self.age}"

  @abstractmethod
  def speak(lang):
    pass

  @abstractmethod
  def eat(food):
    pass

# parent class
class Citizen:
  def __init__(self, passportNo):
    self.passportNo = passportNo

# child or sub class
class Employee(Person, Citizen):
  def __init__(self, name, age, passportNo, salary, id):
    # parent class constructor - only when we have one parent class
    # super().__init__(name, age)

    # mutiple parent classes
    Person.__init__(self, name, age)
    Citizen.__init__(self, passportNo)

    # additional properties for the child constructor
    self.salary = salary
    self.id = id

  def empInfo(self):
    return f"{self.name} of {self.age} years old having an id of {self.id} with salary of ${self.salary}"

  def speak(self, lang):
    return f"{self.name} speaks {lang}"
  
  def eat(self, food):
    return f"{self.name} eats {food}"

emp1 = Employee("Peter", 20, "FDKLJF745424",  20000, "P123")

print(emp1.name)
print(emp1.age)
print(emp1.info())
print(emp1.salary)
print(emp1.id)
print(emp1.empInfo())
print(emp1.passportNo)
print(emp1.speak("Tamil"))
print(emp1.eat("Pizza"))


