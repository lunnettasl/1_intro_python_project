# menu.py

from transaction import Transaction

def display_menu():
    """
    Display the menu options for the user.
    """
    print("\nOptions:")
    print("1. Add item")
    print("2. Update item name")
    print("3. Update item quantity")
    print("4. Update item price")
    print("5. Delete item")
    print("6. Reset transaction")
    print("7. Check order")
    print("8. Print order")
    print("9. Show total price")
    print("0. Exit")

def handle_choice(choice, transaction):
    """
    Handle the user's menu choice.
    
    Parameters:
    choice (str): The menu option chosen by the user.
    transaction (Transaction): The transaction object to perform operations on.
    """
    if choice == '1':
        name = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        price = int(input("Enter price per item: "))
        transaction.add_item(name, qty, price)
    
    elif choice == '2':
        old_name = input("Enter the current item name: ")
        new_name = input("Enter the new item name: ")
        transaction.update_item_name(old_name, new_name)
    
    elif choice == '3':
        name = input("Enter item name: ")
        qty = int(input("Enter new quantity: "))
        transaction.update_item_qty(name, qty)
    
    elif choice == '4':
        name = input("Enter item name: ")
        price = int(input("Enter new price per item: "))
        transaction.update_item_price(name, price)
    
    elif choice == '5':
        name = input("Enter item name to delete: ")
        transaction.delete_item(name)
    
    elif choice == '6':
        print(transaction.reset_transaction())
    
    elif choice == '7':
        print(transaction.check_order())
    
    elif choice == '8':
        transaction.print_order()
    
    elif choice == '9':
        transaction.print_total_price()
    
    elif choice == '0':
        return False
    
    else:
        print("Invalid option. Please try again.")
    
    return True
