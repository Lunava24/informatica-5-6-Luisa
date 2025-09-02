def main():
    message = input("Type a message").lower()
    encode_message(message)

def encode_message(text): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    new_message = ""
    i = 0

    while i < len(text):
        char = text[i]



main()