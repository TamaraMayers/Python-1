


#You are tasked with creating a sample inventory management system for a market. The system should allow users to add, update, view, and remove items from the inventory. Each item in the inventory will have a name, price, quantity, and category.
#Functionality:
        #Add Item: Create a function add_item that allows users to add a new item to the inventory. Users should input the name, price, quantity, and category of the item.
        #Update Item: Implement function update_item that allows to update he details of an existing item in the inventory. Users should be able to update the price, quantity, and category of the item.
        #View Inventory: Develop a function view_inventory that displays all items in the inventory along with their details (name, price, quantity, and category).
        #Remove Item: Create a function remove_item that allows users to remove an item from the inventory based on its name.
        #Search by Category: Implement a function search_by_category that allows users to search for items in the inventory based on their category. The function should display all items belonging to the specified category.

#Project Structure:
        #Define a list inventory to store the items in the market inventory. Each item should be represented as a dictionary with keys for name, price, quantity, and category.
        #Implement the functions add_item, update_item, view_inventory, remove_item and search_by_category to manage the inventory.
        #Create a main loop tp interact with the user. The loop should prompt the user to choose from the various options such as adding, updating, viewing, removing items, or searching by category.



#intializa an empty inventory
inventory = []

#Function to add an item to the inventory
def add_item(name,price,quantity,category):
    item = {
        'name': name,
        "price": price,
        'quantity': quantity,
        'category': category,
    }
    inventory.append(item)
    print(f"Added item: {item['name']}")

#Function to update an existing item
def update_item(name, price=None, quantity=None, category=None):
    for item in inventory:
        if item['name'] == name:
            if price is not None:
                item['price'] = price
            if quantity is not None:
                item['quantity'] = quantity
            if category is not None:
                item['category'] = category
            print(f"Updated item: {item}")
            return
    print("Item not found.")

#Function to view all items in the inventory
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("\nInventory:")
    for item in inventory:
        print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}, Category: {item['category']}")

#Function to remove an item from the inventory
def remove_item(name):
    global inventory
    for item in inventory:
        if item['name'] == name:
            inventory. remove(item)
            print(f"Removed item: {name}")
            return
    print("Item not found.")

#Function to search for items by category
def search_by_category(category):
    found_items = [item for item in inventory if item['category'] == category]
    if found_items:
        print (f"\nitems in category '{category}':")
        for item in found_items:
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
    else:
        print(f"No items found in category '{category}'.")

#Main loop to interact with the user
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            try:
                name = input("Enter item name: ")
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                category = input("Enter item category: ")
                add_item(name, price, quantity, category)
            except ValueError:
                print("Invalid input! Make sure to enter the correct data types.")

        elif choice == '2':
            name = input("Enter item name to update:")
            price = input("Enter new price (or press Enter to skip): ")
            quantity = int(input("Enter item quantity (or press Enter to skip): "))
            category = input("Enter new category (or press Enter to skip): ")
            update_item(name, float(price) if price else None, int(quantity) if quantity else None, category if category else None)

        elif choice == '3':
            view_inventory()

        elif choice == '4':
            name = input("Enter item name to remove: ")
            remove_item(name)

        elif choice == '5':
            category = input("Enter category to search: ")
            search_by_category(category)

        elif choice == '6':
            print("Exiting the inventory management system.")
            break

        else:
            print("Invalid option, please try again.")

#Run the main function.
if __name__ == "__main__":
    main()
