items = ["milk", "bread", "egg"]
prices = [40, 25, 5]
total = 0
print("Available items:")
for i in range(len(items)):
    print(f"{items[i]}: ₹{prices[i]}")
while True:
    bought_item = input("\nEnter the item you bought(or type 'done to finish): ").lower()
    if bought_item == 'done':
        break
    if bought_item in items:
        index = items.index(bought_item) 
        try:
            quantity = int(input(f"Enter quantity of {bought_item}: "))
            if quantity < 0:
                print("Quantity cannot be negative. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number for quantity.")
            continue
        total += prices[index] * quantity
    else:
        print("Sorry, we don't have that item. Please try again.")
print(f"\nTotal bill before discount: ₹{total}")
if total > 1000:
    discount = 0.20
elif total > 500:
    discount = 0.10
else:
    discount = 0.0
discount_amount = total * discount
final_total = total - discount_amount
print(f"Discount applied: {discount*100}%")
print(f"Discount amount: ₹{discount_amount:.2f}")
print(f"Final bill amount: ₹{final_total:.2f}")
