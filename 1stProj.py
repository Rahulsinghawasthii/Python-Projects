menu = {
    'Pasta': 40,
    'Pizza' : 50,
    'Samosa': 20,
    'Coffee' : 50,
    'Salad': 30,
    'Burger' : 40,
    'Coke': 45,
}

#greet
print("Welcome to FAV RESTRO")
print("Pasta: Rs40\nPizza: Rs50\nSamosa: Rs20\nCoffee: Rs50\nSalad: Rs30\nBurger: Rs40\nCoke: Rs45")


order_total = 0
#40 + 50 = 90


item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]     #0 + 40
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")

    else:
        print(f"Ordered item {item_2} is not available yet")

# another_order = input("Do you want to add another item? (Yes/No)")

# if another_order == "Yes":
#     item_3 = input("Enter the name of third item =")
#     if item_3 in menu:
#         order_total += menu[item_3]
#         print(f"Item {item_3} has been added to your order")


print(f"The total amount of items is {order_total}")  
print(f"Thank You Sir! Please Come Again")