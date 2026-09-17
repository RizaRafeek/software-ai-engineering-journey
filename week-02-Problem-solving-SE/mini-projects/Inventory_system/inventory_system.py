products = {}
def add_product():
    product = input("Enter your product")
    quantity = int(input("Enter the quantity"))
    products[product] = quantity

def remove_product():
    rem_prod = input("Enter the name of the product to be removed:")
    del products[rem_prod]

def update_quantity():
    update_prod_name = input("Enter the product name to update:")
    update_prod_quantity = int(input("Enter the updated quantity:"))
    products[update_prod_name] = update_prod_quantity

def search_product():
    search_prod = input("Enter the name of the product to be searched:")
    return products.get(search_prod)

def find_low_stock_products():
    for name, quantity in products.items():
        if quantity < 12:
            print(f"{name}:{quantity}")
            