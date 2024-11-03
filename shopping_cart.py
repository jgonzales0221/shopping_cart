from item_to_purchase import ItemToPurchase  
from datetime import datetime  

class ShoppingCart:
    
    # Initialize the shopping cart with customer name, date, and empty list for cart items
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []  # List to store items added to the cart

    # Method to add an item to the cart
    def add_item(self, item):
        self.cart_items.append(item)

    # Method to remove an item from the cart by item name
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name.lower() == item_name.lower():  # Check if item exists in cart
                self.cart_items.remove(item)  # Remove item if found
                return
        print("Item not found in cart. Nothing removed.")  # Print message if item is not found

    # Method to modify an existing item in the cart
    def modify_item(self, item_to_modify):
        for item in self.cart_items:
            if item.item_name.lower() == item_to_modify.item_name.lower():  # Find item to modify
                if item_to_modify.item_quantity == 0:  # Remove item if quantity is set to zero
                    self.cart_items.remove(item)
                    print(f"{item.item_name} removed from the cart.")
                    return
                
                # Update item attributes if specified by the modified item
                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description
                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                return
        print("Item not found in cart. Nothing modified.")  # Print message if item is not found

    # Calculate and return the total number of items in the cart
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    
    # Calculate and return the total cost of items in the cart
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    
    # Print the cart's total cost and each item's details
    def print_total(self):
        if not self.cart_items:  # Check if cart is empty
            print("SHOPPING CART IS EMPTY")
            return
            
        # Print customer information and cart details
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        
        for item in self.cart_items:
            total = item.item_price * item.item_quantity  # Calculate total price for item
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${total:.2f}")
        
        print(f"\nTotal: ${self.get_cost_of_cart():.2f}")

    # Print the descriptions of items in the cart
    def print_descriptions(self):
        print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions\n")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

    # Static method to validate and return customer name input
    @staticmethod
    def get_valid_customer_name():
        while True:
            name = input("Enter customer's name: ").strip()
            if name:
                return name  # Return name if valid
            print("ERROR: Customer name cannot be empty. Please try again.")

    # Static method to validate and return date input in required format
    @staticmethod
    def get_valid_date():
        while True:
            date_str = input("\nEnter today's date ('e.g. January 1, 2020'): ").strip()
            try:
                date_obj = datetime.strptime(date_str, "%B %d, %Y")  # Validate date format
                return date_obj.strftime("%B %d, %Y")  # Return formatted date string
            except ValueError:
                print("\nERROR: Invalid date format. Please use format like 'January 16, 2024'")

def main():
    # Prompt for customer's name and date and create ShoppingCart object
    customer_name = ShoppingCart.get_valid_customer_name()
    current_date = ShoppingCart.get_valid_date()
    
    # Instantiate shopping cart with customer name and date
    cart = ShoppingCart(customer_name, current_date)
    print(f"Customer name: {cart.customer_name}")
    print(f"Today's date: {cart.current_date}")

    # Main loop to display menu and perform actions
    while True:
        # Display menu options
        print("\nMENU")
        print("\na - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit\n")
        
        choice = input("Choose an option: ").lower()  # Convert input to lowercase immediately

        if choice == 'q':
            break
            
        elif choice == 'a':
            # Add item to cart
            print("\nADD ITEM TO CART")
            try:
                item_name = input("\nEnter the item name: ")
                item_description = input("Enter the item description: ")
                item_price = float(input("Enter the item price: "))
                item_quantity = int(input("Enter the item quantity: "))
            except ValueError:
                print("ERROR: Price and quantity must be numeric. Please try again.")
                continue

            item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            cart.add_item(item)

        elif choice == 'r':
            # Remove item from cart
            print("\nREMOVE ITEM FROM CART")
            item_name = input("\nEnter name of item to remove: ")
            cart.remove_item(item_name)

        elif choice == 'c':
            # Change item quantity
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name: ")
            try:
                new_quantity = int(input("Enter the new quantity: "))
            except ValueError:
                print("ERROR: Quantity must be an integer. Please try again.")
                continue
            
            modified_item = ItemToPurchase(item_name=item_name, item_quantity=new_quantity)
            cart.modify_item(modified_item)
            
        elif choice == 'o':
            # Output shopping cart details
            print("\nOUTPUT SHOPPING CART\n")
            cart.print_total()
            
        elif choice == 'i':
            # Output item descriptions
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()