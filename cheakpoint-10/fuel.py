def main(): 
    fraction = input("Please type a fraction: ").split("/")
    print("The fraction is:", fraction)
    empty_and_full(fraction)


def empty_and_full(fraction):
    porcent = (fraction[0] / fraction[1]) * 100 



main()