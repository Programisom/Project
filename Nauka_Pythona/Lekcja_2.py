import random

problem = 1
while True:
    solve = []
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    mode = random.randint(1, 4)
    if mode == 1:
        c = a + b
        solve.append(a)
        solve.append("+")
        solve.append(b)
    elif mode == 2:
        c = a - b
        solve.append(a)
        solve.append("-")
        solve.append(b)
    elif mode == 3:
        c = a * b
        solve.append(a)
        solve.append("*")
        solve.append(b)
    elif mode == 4:
        if b == 0:  # Unikanie dzielenia przez zero
            continue
        c = round(a / b, 2)  # Zaokrąglamy wynik dzielenia do 2 miejsc po przecinku
        solve.append(a)
        solve.append("/")
        solve.append(b)

    print(" ".join(map(str, solve)))  # Łączymy elementy listy w string

    try:
        answer = float(input(f"Pytanie nr {problem}: "))
    except ValueError:
        print("Podaj poprawną liczbę!")
        continue

    problem += 1

    if round(answer, 2) == round(c, 2):  # Porównujemy zaokrąglone wartości
        print("Dobrze!")
    else:
        print(f"Źle! Powinno być: {c}")