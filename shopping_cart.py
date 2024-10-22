from item_to_purchase import ItemToPurchase
from datetime import datetime

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    def add_item(self, item):
        self.cart_items.append(item)
    
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("ERROR: Item not found in cart. Nothing removed.")
    
    def modify_item(self, item_to_modify):
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description
                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                return
        print("ERROR: Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost
    
    def print_total(self):
        if not self.cart_items:
            print("Your shopping cart is empty!")
            return
            
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"\nNumber of Items: {self.get_num_items_in_cart()}\n")
        
        for item in self.cart_items:
            total = item.item_price * item.item_quantity
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${total}")
        
        print(f"\nTotal: ${self.get_cost_of_cart()}")
    
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions\n")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        
        choice = input("\nChoose an option: ")
        
        if choice == 'q':
            break
        elif choice == 'o':
            print("\nOUTPUT SHOPPING CART\n")
            cart.print_total()
        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS\n")
            cart.print_descriptions()
        elif choice == 'a':
            try:
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                item = ItemToPurchase(name, price, quantity, description)
                cart.add_item(item)
            except ValueError:
                print("ERROR: Price must be a number and quantity must be an integer.")
        elif choice == 'r':
            name = input("Enter name of item to remove: ")
            cart.remove_item(name)
        elif choice == 'c':
            try:
                name = input("Enter the item name: ")
                new_quantity = int(input("Enter the new quantity: "))
                item = ItemToPurchase(name, quantity=new_quantity)
                cart.modify_item(item)
            except ValueError:
                print("ERROR: Quantity must be an integer.")
        else:
            print("ERROR: Invalid option. Please try again.")

def get_valid_customer_name():
    while True:
        name = input("Enter customer's name: ").strip()
        if name:
            return name
        print("ERROR: Customer name cannot be empty. Please try again.")

def get_valid_date():
    while True:
        date_str = input("Enter today's date (e.g., 'January 16, 2024'):").strip()
        try:
            # Attempt to parse the date
            date_obj = datetime.strptime(date_str, "%B %d, %Y")
            # Return the date in the desired format
            return date_obj.strftime("%B %d, %Y")
        except ValueError:
            print("Error: Invalid date format. Please use format like 'January 16, 2024'")
            print("Valid months are: January, February, March, April, May, June, July, August, September, October, November, December")

def main():
    customer_name = get_valid_customer_name()
    current_date = get_valid_date()
    
    cart = ShoppingCart(customer_name, current_date)
    
    print("\nCustomer name:", customer_name)
    print("Today's date:", current_date)
    
    print_menu(cart)

if __name__ == "__main__":
    main()