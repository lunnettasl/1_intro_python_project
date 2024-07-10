# 1_intro_python_project
Optional project for introduction to python course.

## 1. Project Background
### Introduction
The Transaction Management System is a simple command-line application designed to help users manage their shopping transactions. It provides functionalities to add, update, delete items, and calculate the total price with applicable discounts. The system ensures that users can track their purchases efficiently and correct any mistakes before finalizing the transaction.
### Objectives
The main objectives of this project are:
1. To provide a user-friendly interface for managing shopping transactions.
2. To allow users to add, update, and delete items in their shopping cart.
3. To enable users to check the correctness of their transaction details.
4. To calculate the total price of the transaction, including any applicable discounts.
5. To practice modular programming by splitting the functionality into separate modules.

## 2. Flowchart


## 3. Code Information
The project is divided into three modules:
### 1. `transaction.py`
This module contains the `Transaction` class, which is responsible for managing the transaction details. It includes methods to add, update, delete items, reset the transaction, check for input errors, and calculate the total price with discounts. The key methods are:
- `add_item(name, qty, price)`: Adds a new item to the transaction.
- `update_item_name(old_name, new_name)`: Updates the name of an existing item.
- `update_item_qty(name, qty)`: Updates the quantity of an existing item.
- `update_item_price(name, price)`: Updates the price of an existing item.
- `delete_item(name)`: Deletes an item from the transaction and shows the remaining items.
- `reset_transaction()`: Clears all items from the transaction.
- `check_order()`: Checks for any input errors in the transaction.
- `print_order()`: Prints the list of items in the transaction.
- `total_price()`: Calculates the total price after discounts.
- `print_total_price()`: Prints a table of all items and the total price with discounts.

### 2. `menu.py`
This module provides the menu interface for the user to interact with the transaction system. It includes functions to display the menu and handle user choices. The key functions are:
- `display_menu()`: Displays the menu options for the user.
- `handle_choice(choice, transaction)`: Handles the user's menu choice and performs the corresponding action on the `Transaction` object.

### 3. `main.py`
This is the main script that runs the application. It initializes the `Transaction` object and enters an infinite loop to display the menu and process user inputs. The key function is:
- `main()`: The main function that runs the application, displaying the menu and handling user choices.

## 4. Usage Instructions
1. Download the three modules and save in the same local folder.
2. Open the application (example: python; Visual Studio Code)
3. Run the main.py script
4. Interact with the Application:
- Follow the on-screen prompts to add items, update items, delete items, reset the transaction, check the order, print the order, and show the total price.
-The menu options are:
  1. Add item
  2. Update item name
  3. Update item quantity
  4. Update item price
  5. Delete item
  6. Reset transaction
  7. Check order
  8. Print order
  9. Show total price
  10. Exit

## 5. Test Case
1. Showing all options:

![1  Menu Awal](https://github.com/lunnettasl/1_intro_python_project/assets/174937297/eb242c59-8455-4aca-931e-5401ebd30fc3)

2. Add item (option 1):

![2  Add Item](https://github.com/lunnettasl/1_intro_python_project/assets/174937297/977ee232-b781-44c6-ab48-6ec84f5bce67)

3. Delete an item (option 5) and show the remain item list:
![3  Delete an Item](https://github.com/lunnettasl/1_intro_python_project/assets/174937297/d85450b1-bbd4-4250-ad71-e26822af0357)

4. Reset  transaction (option 6) and show information:
![6  Reset](https://github.com/lunnettasl/1_intro_python_project/assets/174937297/17c6efd4-9652-4267-a6ae-f3564bb82a4c)

5. Check current order (option 7):

![7  Check order](https://github.com/lunnettasl/1_intro_python_project/assets/174937297/457fa36b-fc53-4a7b-839c-c635019a72d0)

6. Print order (option 8) and show all the order list:
![8  Print Order](https://github.com/lunnettasl/1_intro_python_project/assets/174937297/38df6fde-4b37-43e9-9f17-e3a8a6f06b69)

7. Show total price (option 9) and show all the order list:
![9  Show total price](https://github.com/lunnettasl/1_intro_python_project/assets/174937297/cc10f309-0caf-48df-ab4e-9faf83550e4c)

## 6. Conclusion and Future Works:
### Conclusion
The Transaction Management System provides a straightforward and effective way to manage shopping transactions using simple modules.

### Future works
1. Adding a graphical user interface (GUI) for a more user-friendly experience.
2. Implementing a database to store transaction history or past transactions.
