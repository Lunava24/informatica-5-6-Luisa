#SyntaxError
# print("Hello, world)

#ValueError
# try:
#     x = int(input("What's x? "))
#     print(f"x is equal to {x}")
# except ValueError:
#     print("x is not a number")


#ZeroDivisionError
# def spam(divide_by):
#     try:
#         return 42 / divide_by
#     except ZeroDivisionError:
#         print("Error: Invalid argument")

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not a number")
    else:
        break

print(f"x is equal to {x}")