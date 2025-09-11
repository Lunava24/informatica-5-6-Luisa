my_list = [5, 2, 3, 1, 4]
my_list2 = ["a", "b", "c"]
greatest = max(my_list) #max is to find the greatest value element in a list
print("The gratest number in the list is: ", greatest)

smallest = min(my_list)
print("The smallest number in the list is: ", smallest)

list_sum = sum(my_list)
print("The sum of all numbers im the list is: ", list_sum)

list_length = len(my_list)
print("This list has ", list_length, "elements.")

in_order = sorted(my_list)           #my_list.sort() --> my_list sorted
print(in_order)                      #sorted(my_list) --> create a copy of my_list and sort it 

def filter_price(price):
    if (price >= 400):
        return True
    else:
        return False

item_price = [230, 400, 450, 350, 370]
filterded_price = filter(filter_price, item_price)
print(list(filterded_price))