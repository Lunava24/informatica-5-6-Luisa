birthdays = {
    "Jazmin": "January 5",
    "Luna": "January 22",
    "Rodrigo": "September 10"
}
for name in birthdays:
    name.find(input("Select a name: "))
    print(f"{name}: {birthdays[name]}")
    # if name in birthdays:

