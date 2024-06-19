class Work:
    def spam(self, point, color):
        print(f"Brawo zarobiłeś *{point}* za zastrzelenie {color}")

# Tworzenie instancji klasy Work
work_instance = Work()

points = 0
color = input("Podaj kolor")
color = color.lower()
print(color)

if color == "zielony" or color == "green":
    work_instance.spam(5, "zielonego")
    points += 5
elif color == "żółty" or color == "yellow":
    work_instance.spam(10, "żółtego")
    points += 10
else:
    print("WoW to było EXITING!!! Masz 10 POINTS!!!")
    points += 10

print(f"Masz: {points} POINTS!!!")
for a in range(1000)
	pass
