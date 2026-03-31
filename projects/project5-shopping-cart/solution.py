# Project 5 — Mini Shopping Cart
# Author: your name here

menu = {
    1: ("Apple",  0.50),
    2: ("Banana", 0.30),
    3: ("Milk",   1.20),
    4: ("Bread",  2.00),
}

cart  = {}   # { item_name: quantity }
total = 0.0

# TODO: display the menu
# print("--- Shop Menu ---")
# for number, (name, price) in menu.items():
#     print(f"{number}. {name:<10} ${price:.2f}")
# print("5. Done")
print("--- Shop Menu ---")
for number, (name, price) in menu.items():
    print(f"{number}. {name:<10} ${price:.2f}")
print("5. Done")
# TODO: shopping loop
# while True:
#     choice = int(input("\nChoose an item (1-5): "))
#     if choice == 5:
#         break
#     if choice in menu:
#         ...add to cart, update total...
#     else:
#         print("Invalid choice, try again.")
while True:
    choice = int(input("\nChoose an item (1-5): "))
    
    if choice == 5:
        break
    
    if choice in menu:
        # Get item details from the menu
        name, price = menu[choice]
        
        # Update the total price
        total += price
        
        # Add to cart and update quantity
        if name in cart:
            cart[name] += 1
        else:
            cart[name] = 1
            
        print(f"Added {name} to your cart.")
    else:
        print("Invalid choice, try again.")

# TODO: print the receipt
# print("\n--- Receipt ---")
# for item, qty in cart.items():
#     ...
# print(f"Total: ${total:.2f}")
# print("Thank you!")
print("\n--- Receipt ---")
for item, qty in cart.items():
    print(f"{item:<10} x{qty}")

print(f"Total: ${total:.2f}")
print("Thank you!")