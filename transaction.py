# transaction.py

class Transaction:
    def __init__(self):
        """
        Initialize the Transaction class with an empty dictionary to store items.
        """
        self.items = {}

    def add_item(self, name, qty, price):
        """
        Add a new item to the transaction.
        
        Parameters:
        name (str): The name of the item.
        qty (int): The quantity of the item.
        price (int): The price per item.
        """
        self.items[name] = [qty, price]

    def update_item_name(self, old_name, new_name):
        """
        Update the name of an existing item.
        
        Parameters:
        old_name (str): The current name of the item.
        new_name (str): The new name for the item.
        """
        if old_name in self.items:
            self.items[new_name] = self.items.pop(old_name)

    def update_item_qty(self, name, qty):
        """
        Update the quantity of an existing item.
        
        Parameters:
        name (str): The name of the item.
        qty (int): The new quantity for the item.
        """
        if name in self.items:
            self.items[name][0] = qty

    def update_item_price(self, name, price):
        """
        Update the price of an existing item.
        
        Parameters:
        name (str): The name of the item.
        price (int): The new price for the item.
        """
        if name in self.items:
            self.items[name][1] = price

    def delete_item(self, name):
        """
        Delete an item from the transaction.
        
        Parameters:
        name (str): The name of the item to be deleted.
        """
        if name in self.items:
            del self.items[name]
            self.print_order()

    def reset_transaction(self):
        """
        Reset the transaction by clearing all items.
        
        Returns:
        str: Confirmation message that all items have been deleted.
        """
        self.items = {}
        return "Semua item berhasil di delete!"

    def check_order(self):
        """
        Check the order for any input errors.
        
        Returns:
        str: Message indicating whether the order is correct or if there are input errors.
        """
        for name, details in self.items.items():
            if not name or details[0] <= 0 or details[1] <= 0:
                return "Terdapat kesalahan input data"
        return "Pemesanan sudah benar"

    def print_order(self):
        """
        Print the list of items in the order.
        """
        print("Item yang dibeli adalah:")
        for name, details in self.items.items():
            print(f"{name}: {details}")

    def total_price(self):
        """
        Calculate the total price of the transaction, applying any applicable discounts.
        
        Returns:
        float: The total price after discounts.
        """
        total = sum(qty * price for qty, price in self.items.values())
        if total > 500000:
            discount = 0.10
        elif total > 300000:
            discount = 0.08
        elif total > 200000:
            discount = 0.05
        else:
            discount = 0.0
        total_with_discount = total * (1 - discount)
        return total, total_with_discount

    def print_total_price(self):
        """
        Print a table of all items with quantity, price per item, and total price.
        Also prints the total price after discount.
        """
        print("\n| No | Nama Item   | Jumlah Item | Harga/Item | Total Harga |")
        print("|----|-------------|-------------|------------|-------------|")
        total = 0
        for i, (name, details) in enumerate(self.items.items(), 1):
            qty, price = details
            total_price = qty * price
            total += total_price
            print(f"| {i:2} | {name:11} | {qty:11} | {price:10} | {total_price:11} |")

        if total > 500000:
            discount = 0.10
        elif total > 300000:
            discount = 0.08
        elif total > 200000:
            discount = 0.05
        else:
            discount = 0.0
        
        total_with_discount = total * (1 - discount)
        print(f"\nTotal belanja yang harus dibayarkan adalah Rp {total_with_discount:.2f} (diskon {discount*100:.0f}%)")
