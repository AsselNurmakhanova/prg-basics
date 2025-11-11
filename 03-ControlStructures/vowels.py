###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
char = text[0]
# Count vowels in the text
while char in text:
    if char in vowels:
        vowel_count += 1
    char = text[text.index(char) + 1] if text.index(char) + 1 < len(text) else None

print(f"The number of vowels in the text is: {vowel_count}")
