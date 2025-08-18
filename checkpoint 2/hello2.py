def hello():
    print("hello")

name = input("What's your name? ").strip().title()
hello()
print(f"hello, {name}")