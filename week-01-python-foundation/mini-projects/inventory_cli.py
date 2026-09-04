Inventory = {}

def load_inventory():
    with open("inventory.txt", "r") as file:
        file_contents = file.read()
        

def save_inventory():
    with open ("inventory.txt", "w") as file:
        for product_name, product_details in Inventory.items():
            file.write(f"{product_name} : {product_details}\n")

def add_product():
    product_name = input("Enter product name: ")
    product_quantity = int(input("Enter your product quantity: "))
    product_price = float(input("Enter your product price: "))
    product_details = {
        "name": product_name,
        "quantity": product_quantity,
        "price": product_price
    }
    Inventory[product_name] = product_details
    save_inventory()
    print(f"{product_name} added successfully!")

def remove_product():
    remove_name = input("Enter the name of the product to be removed: ")
    if remove_name in Inventory:
        del Inventory[remove_name]
        print(f"{remove_name} has been removed from the Inventory.")
    else:
        print(f"{remove_name} is not found in the Inventory.")

def update_quantity():
    update_product = input("Enter the product name to update the quantity: ")
    if update_product in Inventory:
        updated_quantity = int(input("Enter the updated quantity: "))
        Inventory[update_product]["quantity"] = updated_quantity
        print(f"{update_product} quantity has been updated to {updated_quantity}.")
    else:
        print(f"{update_product} is not found in the Inventory.")

def find_product():
    find_name = input("Enter the name of the product to be found: ")
    if find_name in Inventory:
        print(f"{find_name} is found: Inventory details : {Inventory[find_name]}")
    else:
        print(f"{find_name} is not found in the Inventory.")

def display_inventory():
    print("\nCurrent Inventory:")
    if not Inventory:
        print("Your inventory is empty.")
    else:
        print(Inventory)

# Wrapped in a loop so you can use the system continuously
while True:
    print("\nEnter your choice:")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Update Quantity")
    print("4. Find Product")
    print("5. Display Inventory")
    print("6. Exit")
    
    choice = input("Your Choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        remove_product()
    elif choice == "3":
        update_quantity()
    elif choice == "4":
        find_product()
    elif choice == "5":
        display_inventory()  # FIXED: Completed the missing call
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please select 1-6.")
