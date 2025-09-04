def main():
    num = int(input("Enter a positive number: "))
   
    if num < -num:
        num = num * -1

    counter = 1
    while counter <= 10:
        counter2 = 1
        while counter2 <= 10:
            print(f"{counter} * {counter2} = {counter * counter2}")
            counter2 += 1
        counter += 1
        print()

main()
