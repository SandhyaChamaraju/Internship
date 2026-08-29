# 1. Take the post input from the user
post = input("Enter your post: ")

# 2. Check if "harry" is in the post (case-insensitive)
# .lower() converts the text to lowercase so matching is bulletproof
if "harry" in post.lower():
    print("Yes! The post is talking about Harry.")
else:
    print("No! The post does not mention Harry.")
