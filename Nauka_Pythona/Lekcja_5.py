class Flowers:      # Tworzy klasę Flowers
    def __init__(self, name, types, colour, easy_to_plant):  # Konstruktor robi obiekt
        self.name = name
        self.types = types
        self.colour = colour
        self.easy_to_plant = easy_to_plant

    def show_plants(self):  # pokazuje nazwy
        print(f" {self.name}, to: {self.types}\nMa kolor {self.colour} i jest {self.easy_to_plant} w uprawie")


a = input("nazwa: ")
b = input("typ: ")
c = input("kolor: ")
d = input("poziom uprawiania: ")
my_flowers = Flowers(a, b, c, d)  # klasa flowers zmienia się w zmienną my flowers
my_flowers.__init__(a, b, c, d)    # przypisania
my_flowers.show_plants()    # wywołuje funkcje
