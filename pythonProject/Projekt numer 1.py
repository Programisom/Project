class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

# Tworzenie obiektów zwierząt
dog = Dog("Rex")
cat = Cat("Whiskers")

# Symulacja wydawania dźwięków
dog.make_sound(f)
cat.make_sound()