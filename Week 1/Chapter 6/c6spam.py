def is_spam(comment):
  spam_keywords = ["po make a lot of money", "buy now", "subscribe this", "click this"]
  comment_lower = comment.lower()

  for keyword in spam_keywords:
    if keyword in comment_lower:
      return True  # Spam detected

  return False  # Not spam



sample_comment = "Hey guys, click this link to buy now and make money!"

if is_spam(sample_comment):
  print("Spam detected!")
else:
  print("Clean comment.")
