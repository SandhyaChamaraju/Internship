def remove_word(words, word):
    words = [item.strip() for item in words if item.strip() != word]
    return words

my_list = [" apple ", "banana", " apple", "orange "]
print(remove_word(my_list, "apple"))
