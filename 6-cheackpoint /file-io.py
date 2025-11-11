#names = []

#for i in range(3): #make lists "range"
    #names.append(input("What's your name? "))

#for name in sorted(names):
    #print(f"Hello {name}")

# name = input("What's your name? ")
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# with open("name.txt", "a") as file:  #(file is a variable)
#     file.write(f"{input("What's your name? ")}")  #


with open("names.txt", "r") as file:
    lines = file.readlines() 

for line in sorted(lines):
    print(f"Hello {line.rsplit()}")
