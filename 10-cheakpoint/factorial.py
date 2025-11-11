# def divide(a,b):
#     if b == 0:
#         raise ValueError("Hey! You cannot divided by zero.")
#     return a / b

# print(divide(1,2))
# print(divide(2,0))



def main():
    result = 1
    num = int(input("Type an interger number: "))
    if num < 0:
        raise ValueError("Hey! You cannot use negative numbers.")
    for number in range(1,num + 1):
        result = result * number

    print(result)
main()