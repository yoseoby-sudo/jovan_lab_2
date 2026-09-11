inventory = 0
rejected = 0
print ("Welcome to inventory taking")

while True:

    inventory_input = input("Enter stock: ")

    #Check for quit condition
    if inventory_input.lower() == "quit":
        break

    # Check if input is a valid number try: 
    try:
        quantity = int(inventory_input)
    except ValueError:
        print("Error, Inventory must be a number")
        rejected += 1
        continue

    #Validate that number is not negative
    quantity = int(inventory_input)
    if quantity < 0:
        print("Error , Inventory cannot be negative")
        rejected += 1
        continue

    #Check if adding the quantity exceeds the maximum inventory limit
    inventory += quantity
    if inventory > 500:
        print("Inventory overloaded!")
        break

print(f"Total Inventory Entered: {inventory}")
print(f"Rejected Inventory Entries: {rejected}")