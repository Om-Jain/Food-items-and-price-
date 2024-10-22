choice = int(input("Enter the choice from 1 to 5: "))
quantity = int(input("Enter the quantity required: "))

# Initialize ticket prices
menu = {
    1: ("Pizza", 200),
    2: ("Burger", 100),
    3: ("Dosa", 150),
    4: ("Briyani", 250),
    5: ("Chicken Rice", 200)
}

# Calculate total cost
intem_name, item_price = menu[choice]
total_cost = item_price * quantity

# Check for discount

discount = 0
if total_cost > 500:
    discount = total_cost * 0.1

# Display the discount
final_cost = total_cost - discount

# Display the total cost
print(f"Total cost for food: {total_cost}")

if discount > 0:
    print(f"Discount: {discount}")
print(f"Final cost: {final_cost}")