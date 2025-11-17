def f(amount_to_pay):
    total = 0
    num_5 = amount_to_pay // 5
    remaining = amount_to_pay % 5
    num_2 = remaining // 2
    remaining = remaining % 2
    num_1 = remaining
    total = num_5 + num_2 + num_1
    return total