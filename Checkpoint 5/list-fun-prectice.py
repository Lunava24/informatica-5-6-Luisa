def length (list):
    list_lenght = len(list)
    return list_lenght

def mean (list): 
    integers = len(list)
    return integers
    
def range_of_list(list):
    return (f"{min(list)} - {max(list)}")

def main():
    list = []
    while True:
        word = int(input("Type numberst to add to list: "))
        if word == 0:
            break
        list.append(word)
        print(list)
        print(sorted(list))

    print(length(list))
    print(mean(list))
    print(range_of_list(list))

main()

