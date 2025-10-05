message = input("Send a message: ")
filename = "message.txt"

with open(filename, 'w') as file:
    file.write(message)

with open(filename, "r") as file:
    message = file.readline().strip()

dictionary = {}
for character in message:
    dictionary[character] = dictionary.get(character, 0) + 1
print(dictionary)

print(len(message))

find = max(dictionary, key=dictionary.get)
print(f"The largest word is: {find}, It appears: {dictionary[find]} times") 
