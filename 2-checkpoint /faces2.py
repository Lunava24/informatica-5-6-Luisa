def main():
    emoji = input("Write a message with an emotion: ")
    convert(emoji)

    def convert(message):
        message = message.replace(":)","🙂").replace(":(", "🙁")
        print(message)

main()
