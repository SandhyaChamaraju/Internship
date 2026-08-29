# Create Hindi to English dictionary
hindi_dict = {
    "namaste": "Hello",
    "kitab": "Book", 
    "pani": "Water",
    "ghar": "House",
    "dhanyawad": "Thank you",
}


while True:
  word = input("\nEnter a Hindi word to search (or type 'exit' to quit): ")

  if word.lower() == "exit":
    print("Goodbye!")
    break

  if word in hindi_dict:
    print(f"Meaning: {hindi_dict[word]}")
  else:
    print("Word not found in the dictionary.")
