import random
dice_roll = random.randint(1, 6)
special = dice_roll == 6 or dice_roll == 1
print("Dice rolled:", dice_roll)
print("Special number (1 or 6):", special)