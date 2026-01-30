import random
import utill_functions
def main():
		easterEggCount = 15
		maxGuessCount = 20
		minGuess = 1
		maxGuess = 100
		playCount = 0
		while True:
			if playCount == easterEggCount:
					print("WHY DID YOU WASTE YOUR TIME ON THIS DUMB GAME! DO SOMETHING BETTER WITH YOUR TIME!")
					quit()
			playCount += 1
			num = random.randint (minGuess,maxGuess)
			print(f'Welcome the GUESS THE NUMBER! You have {maxGuessCount} attempts before you lose the game. good luck.')
			guess = utill_functions.get_valid_type(int,f'Guess a number {minGuess}-{maxGuess}: ',"that is not a number") 
			for _ in range(maxGuessCount): 
				if guess < num:
					guess = int(input("the number is larger: "))
				if guess > num:
					guess = int(input("the number is smaller: "))
				if guess == num : 
					print ("you got it")	
					playgain = str(input("do you want to play again? (y/n): "))
					if playgain.lower() == "n":
						return
					else:
						print("ok")
							
if __name__=="__main__":
    main()