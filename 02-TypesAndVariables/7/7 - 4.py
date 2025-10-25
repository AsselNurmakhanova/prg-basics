circumference = float(input("Enter tree circumference in cm: "))
diameter = circumference / 3.14159
can_cut = diameter >= 50
print("Tree can be cut down:", can_cut)