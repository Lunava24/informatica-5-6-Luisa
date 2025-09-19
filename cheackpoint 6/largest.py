list_length = int(input("List length: "))
numbers_list = []

for numbers in range(list_length):
    list_element = int(input("Enter element: "))
    numbers_list.append(list_element)

print(numbers_list)

with open("largest.txt", "a") as file:  
    file.write(f"{input("What's the largest number? ")}")
