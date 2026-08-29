def game():
    # Game code goes here
    score = int(input("Enter your score: "))
    return score


score = game()

with open("HiScore.txt", "r") as f:
    content = f.read()

if content == "":
    high_score = 0
else:
    high_score = int(content)

if score > high_score:
    print("New High Score!")
    with open("HiScore.txt", "w") as f:
        f.write(str(score))
else:
    print("High Score:", high_score)
