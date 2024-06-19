i = "a"
print("Wpisz roślinę, a ja ją rozpoznam")


def recognize_plant(plant):
    if plant == "Sosna":
        print(f"To jest {plant}. Jest ona iglasta")

    elif plant == "Świerk":
        print(f"To jest {plant}. Jest ona iglasta")

    elif plant == "*":
        pass

    elif plant == "Stokrotka":
        print("To jest kwiatek z białymi płatkami")

    else:
        print("Nie mam tego w bazie danych")


while i != "*":
    print("Wpisz '*' aby wyjść")
    i = input("")
    i = i.title()
    recognize_plant(i)



