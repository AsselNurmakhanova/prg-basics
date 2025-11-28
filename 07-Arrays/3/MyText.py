def number_of_words(text):
    count = 0
    for i in text:
        if i == ' ':
            count += 1
    return count + 1

def longest_array_of_words(text):
    words = text.split()
    n = len(words)
    for i in range(n-1):
        for j in range(n-1-i):
            if len(words[j]) < len(words[j+1]):
                words[j], words[j+1] = words[j+1], words[j]
    return words

def sort_words_alphabetically(text):
    words = text.split()      # разбиваем текст на слова
    words.sort()              # сортируем список слов по алфавиту
    return words

