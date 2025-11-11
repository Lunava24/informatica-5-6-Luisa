def main():
    number = int(input("set password: "))
    check_password(number)

def check_password(password):
    word = int(input("What is the password?: "))
    if password == word:
        print("you got the correct password")

    if password != word:
        print("your password is incorrect")

main()

