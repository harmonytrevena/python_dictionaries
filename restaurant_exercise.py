menu = {
    "Brunch" : {
    "Steak and Eggs": 16.99,
    "Three Egg Breakfast": 8.99,
    "Egg Benedict": 11.99,
    "Biscuit and Gravy": 7.99,
    "Chicken Fingers": 10.99,
    "Chicken Wrap": 8.99,
    "Steak Salad" : 1.99
},
    "Drinks": {
    "Soft Drink": 1.99,
    "Coffee": 1.99,
    "Orange Juice": 0.99,
    "Milk": 0.55,
    "Water": 0.00
    }
}

# Fix the price of the steak salad. It should be 15.99.
menu["Brunch"]["Steak Salad"] = 15.99

# Add a specials menu that includes: Soup of the Day (8.99), Catch of the Day (14.99), Chef Special (15.99)
menu["Special Menu"]={"Soup of the Day": 8.99, "Catch of the Day": 14.99, "Chef Special": 15.99}

# Change "Three Egg Breakfast" to have the options of: Without Bacon (8.99) and With Bacon (9.99)
menu["Brunch"]["Three Egg Breakfast"]={"with Bacon": 9.99, "without Bacon": 8.99}

