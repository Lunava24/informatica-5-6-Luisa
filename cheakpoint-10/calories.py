def main():

    protein_list = {
        "Milk": 73,
        "Almond milk": 30,
        "Sour Cream, light": 16,
        "Plain, low-fat": 77,
        "Egg": 75,
        "Egg white": 16,
        "Cream Cheese": 17,
        "American Pasteurized": 79,
        "Peanuts, roasted": 166,
        "Sunflower seeds, dry roasted": 165,
        "Lentils, boiled": 115,
        "Black beans, boiled": 113,
        "Swai, baked": 89,
        "Catfish, baked": 89,
        "Broccoli": 7,
        "Carrots, raw": 13,
        "Watermelon": 11,
        "Blueberries": 21,
        "Quinoa, cooked": 56,
        "Ranch": 73
    }

    food = input("Choose a food: ").capitalize().strip()
    food_2 = input("Choose a second food: ").capitalize().strip()
    calculate_calories(food, food_2, protein_list)

def calculate_calories(food, food_2, protein_list):

    if food == "Watermelon" or food_2 == "Watermelon" and food_2 == "Milk" or food == "Milk":
        raise ValueError("You use a bad combination.")


    calories = (protein_list[food] + protein_list[food_2])
    print(f"Food: {protein_list[food]}\nFood 2: {protein_list[food_2]}\nTheir Calories: {calories}, ")

main()