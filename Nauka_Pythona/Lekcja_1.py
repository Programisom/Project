import random as rnd

a = True
while True:
    mode = rnd.randint(0, 2)
    to_guess = rnd.randint(0, 9)
    lista = ["Komputer", "Macintosh", "Maciuś", "Dominiczek", "Asia", "Wanda", "Siedemnaście", "Wykop", "Nie", "Tak"]

    if mode == 0:
        lista.reverse()  # Odwracamy listę
    elif mode == 1:
        pass  # Nic nie robimy
    elif mode == 2:
        lista.sort()  # Sortujemy listę rosnąco

    print(f"Tu jest lista: {lista}, zapamiętaj ją ")
    input("Naciśnij Enter, aby kontynuować...")

    # Usuwanie ekranu (działa tylko w konsoli, efekt zależy od systemu operacyjnego)
    print("\n" * 100)

    taken = lista.pop(to_guess)
    print(f"Co zabrałem? {lista}")
    a = input("Podaj brakujący element: ")

    if a == taken:
        print("Gratulacje!!!")
        b = input("Czy chcesz zakończyć? (y/n): ")
        if b.lower() == "y":
            quit("Lekcja_1.py")
    else:
        print(f"Niestety, to nie jest poprawna odpowiedź. Brakowało: {taken}")