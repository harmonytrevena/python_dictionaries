meal = {
    "Drink": "Wine",
    "Appetizer": "Meat and Cheese Board",
    "Entree": "Steak",
    "Dessert": "Chocolate",
}

print(meal)

# if "Dessert" in meal:
#     print("Harmony enjoyed dessert! She ate %s" % (meal["Dessert"]))
# else:
#     print("Harmony, unfortunately, missed out on dessert!")

# if "Dessert" in meal:
#     del meal["Dessert"]
#     print(meal)

# 1. Phonebook Dictionary

phonebook_dict = {
  "Alice": "703-493-1834",
  "Bob": "857-384-1234",
  "Elizabeth": "484-584-2923"
}

# print(phonebook_dict["Alice"])

phonebook_dict["Kareem"] = "938-489-1234"
print(phonebook_dict)

del phonebook_dict["Alice"]
print(phonebook_dict)

phonebook_dict["Bob"] = "938-489-1234"
print(phonebook_dict)
