grocery_inventory = {
    "Milk" : ("Dairy", 3.50, 8),
    "Eggs" : ("Dairy", 5.50, 30),
    "Bread" : ("Bakery", 2.99, 15),
    "Apples" : ("Produce", 1.50, 50)
}

category_eggs, price_eggs, stock_eggs = grocery_inventory.get("Eggs")

if price_eggs > 5.00:
    print("Eggs are too expensive, reducing the price by $1.")
    price_eggs -= 1.00
    grocery_inventory["Eggs"] = (category_eggs, price_eggs, stock_eggs)
else:
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes: ", grocery_inventory)

category_milk, price_milk, stock_milk = grocery_inventory.get("Milk")
if stock_milk < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (category_milk, price_milk, stock_milk + 20)
else:
    print("Milk has sufficient stock.")

category_apples, price_apples, stock_apples = grocery_inventory.get("Apples")
if price_apples > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print("Updated Inventory: ", grocery_inventory)
                                                                    


    
    
