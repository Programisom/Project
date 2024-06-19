users = ["Dominik", "Admin", "Gość"]
password_D = "lo64."
password_A = "mS_98"
password_G = "xyz"

print("Zaloguj się:")

a = input("Email:")
b = input("Hasło:")

for user in users:
    if a == user:
        print(f"Witaj {user}")

else:
    print("User not registred")