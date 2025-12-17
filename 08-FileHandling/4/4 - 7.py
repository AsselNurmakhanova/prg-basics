import re
phrase = input("Enter a phrase: ")
pattern = r'[aeiouAEIOU]'
vowels = re.findall(pattern, phrase)
num_vowels = len(vowels)
print(f"Number of vowels: {num_vowels}")