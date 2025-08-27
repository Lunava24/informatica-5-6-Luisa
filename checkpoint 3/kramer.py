condition = True

while condition:
    greeting = input("Type a greeting")

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"): 
    print("$20")
elif greeting.startswith("other"):
    print("$100")

print("have a good day")

