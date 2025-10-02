message = input("Send a message: ")
dictionary = {}
for character in message:
    dictionary[character] = dictionary.get(character, 0) + 1
print(dictionary)

print(len(message))

find = max(dictionary, key=dictionary.get)
print(f"The largest word is: {find}, It appears: {dictionary[find]} times") 

#
#
#