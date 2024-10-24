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
        print("Item not found in cart. Nothing removed.")
 
    def modify_item(self, item_to_modify):
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                if item_to_modify.item_quantity == 0:
                    self.cart_items.remove(item)
                    print(f"{item.item_name} removed from the cart.")
                    return
                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description
                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
        
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    
    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
            
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        
        for item in self.cart_items:
            total = item.item_price * item.item_quantity
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${total:.2f}")
        
        print(f"\nTotal: ${self.get_cost_of_cart():.2f}")
    
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
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
        
        choice = input("\nChoose an option: ").lower()
        
        if choice == 'q':
            break
        elif choice == 'o':
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()
        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == 'a':
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(item)
        elif choice == 'r':
            name = input("Enter name of item to remove: ")
            cart.remove_item(name)
        elif choice == 'c':
            name = input("Enter the item name: ")
            
            
            for item in cart.cart_items:
                if item.item_name == name:
                    new_quantity = int(input(f"Enter the new quantity for {name}: "))
                    
                    modified_item = ItemToPurchase(name, item.item_price, new_quantity, item.item_description)
                    cart.modify_item(modified_item)
                    break
            else:
                print(f"Item {name} not found in the cart.")
        else:
            print("Invalid option. Please try again.")


def get_valid_customer_name():
    while True:
        name = input("Enter customer's name: ").strip()
        if name:
            return name
        print("ERROR: Customer name cannot be empty. Please try again.")

def get_valid_date():
    while True:
        date_str = input("Enter today's date ('e.g. January 1, 2020'): ").strip()
        try:
            
            date_obj = datetime.strptime(date_str, "%B %d, %Y")
            
            return date_obj.strftime("%B %d, %Y")
        except ValueError:
            print("ERROR: Invalid date format. Please use format like 'January 16, 2024'")
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