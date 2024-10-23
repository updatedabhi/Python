secretNumber = 8
guessCount = 0
guessLimit = 3
while guessCount < guessLimit:
    guess = int(input("Guess: "))
    guessCount += 1
    if secretNumber == guess:
        print("You Won!")
        break
else:
    print("Sorry! You failed")
