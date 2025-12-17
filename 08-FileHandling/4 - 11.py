output_file = "powers.txt"
with open(output_file, 'w') as file:
    for i in range(1, 101):
        square = i ** 2
        cube = i ** 3
        line = f"{i},{square},{cube}"
        print(line)
        file.write(line + "\n")