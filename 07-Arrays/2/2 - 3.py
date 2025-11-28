# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food = 0
transport = 0
utilities = 0
i = 0
for i in monthly_expenses:
    food += i[0]
    transport += i[1]
    utilities += i[2]

for i, week in enumerate(monthly_expenses, start=1):
    week_total = sum(week)
    print(f'Week {i}: {week_total}')

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food)
print('Transport:', transport)
print('Utilities:', utilities)
print('---------------')