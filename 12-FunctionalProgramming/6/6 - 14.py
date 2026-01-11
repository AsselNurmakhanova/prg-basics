capacity = 500
tolerance_percent = 2
bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]
tolerance = capacity * tolerance_percent / 100
min_fill = capacity - tolerance
max_fill = capacity + tolerance
incorrect = list(
    filter(lambda x: x < min_fill or x > max_fill, bottles)
)
percentage = len(incorrect) / len(bottles) * 100
print(f"Bottle capacity:    {capacity}ml")
print(f"Filling tolerance:  {tolerance_percent}%")
print(f"Filled bottles:     {','.join(map(str, bottles))}")
print(f"Incorrectly filled: {int(percentage)}%")
