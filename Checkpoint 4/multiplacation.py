num = int(input("Enter a positive number: "))

if num < -num:
    num = num * -1

counter = 1
while counter <= 10:
    print(f"{num} * {counter} = {num * counter}")
    counter += 1

