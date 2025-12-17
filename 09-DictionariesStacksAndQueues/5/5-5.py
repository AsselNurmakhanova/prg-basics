paragraph = "cat dog mouse cat rat cat mouse"
paragraph_list = paragraph.split()
word_count = {}
for word in paragraph_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)