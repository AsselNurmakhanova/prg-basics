price = float(input("Enter the price: "))
discount = float(input("Enter the discount %: "))
reduction = price * (discount / 100)
new_price = price - reduction
print(f"Enter price: {price:.2f}")
print(f"Enter discount %: {discount:.2f}")
print(f"Price with discount: {new_price:.2f}")
print(f"Reduction: {reduction:.2f}")