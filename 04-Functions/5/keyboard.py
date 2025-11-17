def input_string(prompt):
    value = input(prompt)
    return value


def input_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter an integer number.")


def input_real(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a real number (e.g. 3.14).")


def input_boolean(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ('y'):
            return True
        elif value in ('n'):
            return False
        else:
            print("Please answer 'y' or 'n'.")
