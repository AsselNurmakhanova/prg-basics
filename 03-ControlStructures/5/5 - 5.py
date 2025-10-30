total_sum = 0
count = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  
    total_sum += number
    count += 1
if count > 0:  # to avoid division by zero
    mean = total_sum / count
    print(f"The total sum of the numbers is: {total_sum} and the arithmetic mean of the numbers is: {mean}")
else:
    print("No numbers were entered.")

