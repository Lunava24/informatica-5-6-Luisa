name = input("choose a name: ")
money = 0
coca = 50 

while money < coca: 

    coin = int(input(f"amount due {coca - money} insert a coin"))
    if coin == 50 or 25 or 10 or 5:
        money = money + coin
    else: print("insert correct coin: ")
    if money >= 50:
        print(f"change {money - coca} Here’s a Coke for {name}")
