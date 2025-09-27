birthdays = {
    "Jazmin": "January 5",
    "Luna": "January 22",
    "Rodrigo": "September 10"
}

name = input("Enter a name: ")

if name in birthdays:
    print(f"Name: {name} Birthday: {birthdays[name]}")
else: 
    print("We dont have that name")
    birthdate = input("When was this person born: ")
    birthdays[name] = birthdate
print(birthdays)




