def main():
    length(length(values()))
    mean(values())
    range_of_list(values())

def values():
    value_list = []
    while True:
        value = int(input("Enter a value: "))
        if (value != 0):
            value_list.append(value)
            print(value_list)
            ordered_list = sorted(value_list)
            print(ordered_list)
            continue
        else:
            break
    return value_list

def length(list):
    return len(list)

def mean(list):
    print(sum(list) / len(list))

def range_of_list(list):
    print(max(list) - min(list))

main()