def main():  #Starting a new function
    message = input("Type a message: ").lower() #Get the message 
    encode_message(message) # calling the function


def encode_message(text): #Starting a new function
    alphabet = "abcdefghijklmnopqrstuvwxyz" #This is the alphabet variable 
    cipher = "zyxwvutsrqponmlkjihgfedcba" #Transposing all the letters in the alphabet such that the resulting alphabet is backwards
    new_message = "" # create an empty variable to add the cipher
    i = 0 # Counting of variable index

    while i < len(text): # Count aslong as variable lengh
        char = text[i] # Get the character from the variable

        if char in alphabet: # checks if char is in the alphabet
            cipher_index = alphabet.find(char) # 
            new_message += cipher[cipher_index] #
        else: #
            new_message += char #
        i += 1 #
    print(new_message) #

main() #