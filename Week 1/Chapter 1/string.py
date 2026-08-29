def has_double_space(text):
    return "  " in text

test_string="Hello sandhya"
if has_double_space(test_string):
    print("Double space detected!")
else:
    print("No double space found")
