#parent class 


from abc import abstractmethod


class Animals(ABC):
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display(self):
        print(f"Name: {self.name}, Habitat: {self.habitat}")

    @abstractmethod
    def speak(self):
        pass

#child class 1
class Dog(Animals):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed = breed

    def speak(self):
        print(f"{self.name} ({self.breed}) says Woof! woof!")