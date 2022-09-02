# Quiz Game/Template for quiz game w/ scoring
score = 0
game = input("Want to play the quiz game? ")
if game == "yes" or game == "YES" or game == "Yes":
    print("Great, lets play!")
else: quit()
game = input("What does AWD mean? ") #Pass question as argument in input function
if game == "All Wheel Drive" or game == "all wheel drive":
    print("Correct")
    score += 100
    print("Score: " + str(score))
else: print("Incorrect", "\nScore: " + str(score))
game = input("What color is the T-Mobile logo? ")
if game == "Magenta" or game == "MAGENTA" or game == "magenta":
    print("Correct")
    score += 100
    print("Score: " + str(score))
else: print("Incorrect", "\nScore: " + str(score))
game = input("What state is OK? ")
if game == "oklahoma" or game == "OKLAHOMA" or game == "Oklahoma":
    print("Correct")
    score += 100
    print("Score: " + str(score))
else: print("Incorrect", "\nScore: " + str(score))
game = input("What did amazon first sell? ")
if game == "books" or game == "Books" or game == "BOOKS":
    print("Correct")
    score += 100
    print("Score: " + str(score))
else: print("Incorrect", "\nScore: " + str(score))
print("Final Question:")
game = input("What shape is stewie from Family Guy's head? ")
if game == "football" or game == "FOOTBALL" or game == "Football":
    print("Correct")
    score += 100
    print("Score: " + str(score))
else: print("Incorrect", "\nScore: " + str(score))
if score > 300:
    print("You've won the quiz game, congratulations!!!")
else: print(":-( You've failed the quiz game")