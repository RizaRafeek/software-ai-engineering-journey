from datetime import datetime


def save_to_file():
    pass
def Create_Customer():
    name = input("Enter the name of the customer:")
    id = input("Enter the id of the customer:")
    Email = input("Enter the Email of the Customer:")
    Phone = input("Enter the Phone Number of the Customer: ")
    Created_date = datetime.now()
    new_customer = {
        "name" : name,
        "id" : id,
        "Email" : Email,
        "Phone" : Phone,
        "Created_Date" : Created_date
    }
    save_to_file()
    
def Update_Customer():
    id = input("Enter the id of the customer:")
    id = int(id)
    
    print("Which Information Would you like to update?:")
    print("1.Name")
    print("2.Email")
    print("3.Phone Number")
    u_choice = input("Enter your choice:")

    if u_choice == "1":
        customer["name"] = input("Enter new name:")
    elif u_choice == "2" :
        customer["Email"] = input("Enter new Gmail:")
    elif u_choice == "3":
        customer["Phone"] =  input("Enter new phone number:")


def Delete_Customer():
    pass
def Search_Customer():
    pass
def List_Customers():
    pass


while True:
    print("Enter your Choice:")
    print("1.Create Customer")
    print("2.Update_Customer")
    print("3.Delete Customer")
    print("4.Search Customer")
    print("5.List Customer")
    print("6.Exit")
    choice = input("Enter your choice:")

    if choice == "1":
        Create_Customer()
    elif choice == "2":
        Update_Customer()
    elif choice == "3":
        Delete_Customer()
    elif choice == "4":
        Search_Customer()
    elif choice == "5":
        List_Customers()
    elif choice == "6":
        print("Exiting..")
        break
    else:
        print("Enter Valid Choice from 1-6")
    