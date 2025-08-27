def main():
    x = int(input("Type a number"))


    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
        exit() 
    if x % 3 == 0:
        print("Fuzz") 
    if x % 5 == 0:
        print("Buzz")
    else: print(x) 
               
main()