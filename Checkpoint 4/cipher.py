def main(): #
    message = input("Type a message: ").lower() #This is to start the function
    encode_message(message) # calling the function


def encode_message(text): #Starting a new function
    alphabet = "abcdefghijklmnopqrstuvwxyz" #This is the alphabet variable 
    cipher = "zyxwvutsrqponmlkjihgfedcba" #Transposing all the letters in the alphabet such that the resulting alphabet is backwards
    new_message = "" #
    i = 0 #The first letter is iqual to 0

    while i < len(text): #
        char = text[i] #

        if char in alphabet: #
            cipher_index = alphabet.find(char) #
            new_message += cipher[cipher_index] #
        else: #
            new_message += char #
        i += 1 #
    print(new_message) #

main() #