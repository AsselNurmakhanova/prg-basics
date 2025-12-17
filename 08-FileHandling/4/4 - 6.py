def count_file(filename):
    num_lines = 0
    num_chars = 0
    num_words = 0

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                num_lines += 1
                num_chars += len(line)
                num_words += len(line.split())
        return num_lines, num_chars, num_words
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

# --- Основная программа ---
filename = input("Enter file name: ")
result = count_file(filename)

if result:
    num_lines, num_chars, num_words = result
    print(f"File name: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of characters: {num_chars}")
    print(f"Number of words: {num_words}")
