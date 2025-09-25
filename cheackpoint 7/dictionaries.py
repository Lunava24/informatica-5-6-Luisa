capitals = {
    "Mexico": "Mexico City",
    "Canada": "Ottawa",
    "Brazil": "Brasillia"
    # "Canada": "Montreal"  Use unique keys
} #we are define a key with a value

capitals["Italy"] = "Rome" #add a new key and value
del capitals["Brazil"]#deletes keys and values
capitals.pop("Canada")#deletes keys and values but with 
capitals.clear()#clean all lists

#print(capitals)#with brackets in the parenthesis we will choose a key, then the value

# Houses = {
#     "Hermione": "Griffndor", 
#     "Harry": "Griffndor",
#     "Ron": "Griffndor",
#     "Draco": "Slytherin"
# }

# print(Houses["Draco"])#only print the key

# for key in Houses:
#     print(f"{key}: {Houses[key]}")

students = [
    {"name": "Hermione", "house": "Griffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Griffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Griffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
for element in students:
    print(f"{element["name"]}, {element["house"]}, {element["patronus"]}")