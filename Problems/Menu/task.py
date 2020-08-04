pizza = "Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy"
salad = "Caesar salad, Green salad, Tuna salad, Fruit salad"
soup = "Chicken soup, Ramen, Tomato soup, Mushroom cream soup"
menu = {'pizza': pizza, 'salad': salad, 'soup': soup}
choice = input()
if choice in menu:
    print(menu[choice])
else:
    print("Sorry, we don't have it in the menu")
