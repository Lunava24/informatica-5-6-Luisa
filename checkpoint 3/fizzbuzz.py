def main():
    x = int(input("Type a number"))

    if x % 3:
        print("Fuzz") 
    if x % 5:
        print("Buzz")
    if x % 3 and x % 3:
        print("FizzBuzz")            
