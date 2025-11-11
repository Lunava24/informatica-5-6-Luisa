def main():
    list_length = int(input("List length: "))
    numbers = []
    print(f"Enter {list_length} numbers: ")

    for list in range(list_length):
        number = int(input())
        numbers.append(number)

    with open("largest.txt", "w") as file:
        for num in numbers:  
            file.write(f"{number}\n")
    largest_number = max(numbers)
    print(f"The largest number is: {largest_number} ")

main()