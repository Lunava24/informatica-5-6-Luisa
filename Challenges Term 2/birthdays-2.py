birthdays = {}
while True:
    name = input("Enter a name type 1 to exit: ")
    if name == "1":
        break
    birthdate = input(f"Type a birthdate")
    birthdays[name] = birthdate

with open("birthdays.txt", "w") as file:
    for name, date in birthdays.items():
        file.write(f"{name}: {birthdate},\n")

with open("birthdays.txt", "r") as file:
    line = file.read()
    print(line)