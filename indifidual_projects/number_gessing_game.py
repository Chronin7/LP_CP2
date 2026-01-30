import random
def main():
		easterEggCount = 15
		maxGuessCount = 20
		minGuess = 1
		maxGuess = 100
		playCount = 0
		playAgain = True
		while playAgain == True:
				if playCount == easterEggCount:
						print("WHY DID YOU WASTE YOUR TIME ON THIS DUMB GAME! DO SOMETHING BETTER WITH YOUR TIME!")
						quit()
				playCount += 1
				num = random.randint (minGuess,maxGuess)
				print(f'Welcome the GUESS THE NUMBER! You have {maxGuessCount} attempts before you lose the game. good luck.')
				guess = int(input(f'Guess a number {minGuess}-{maxGuess}: '))  
				for x in range(maxGuessCount): 
					if guess < num:
						guess = int(input("the number is larger: "))
					if guess > num:
						guess = int(input("the number is smaller: "))
					if guess == num : 
						print ("you got it")
						playgain = str(input("do you want to play again? (y/n): "))
						if playgain != "y":
							playAgain = False
							print("ok sending you back to the hub")
							return
						else:
							print("ok")
if __name__=="__main__":
    main()