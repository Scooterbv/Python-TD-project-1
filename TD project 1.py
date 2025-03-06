
import random


def start_game():
	high_score = None
	
	while True:
			print("\n----------------------------------------")
			print("Hi! Welcome to the number guessing game!")
			print("----------------------------------------\n")
			print("In this game you will guess a number between 1-100.")
		
			if high_score:
					print(f"High score to beat is currently {high_score} ")
				
					
					
			print("Can you guess the correct number?")
			num_correct = random.randint(1,100)
			
			attempts = 0
			
			while True:
					try:
							num_guess = int(input("Pick a number between 1 - 100: "))
							if num_guess < 1 or num_guess > 100:
									print("The number is out of range!")
									continue
									
							attempts += 1
							
							if num_guess > num_correct:
									print("It's lower")
							elif num_guess < num_correct:
									print("It's higher")
							else:
									print(f"Got it! Attempts: {attempts}")
									if high_score is None or attempts < high_score:
											high_score = attempts
									break
									
					except ValueError:
							print("Invalid input!")
	
				
			play_again = input("Would you like to play again? yes/no: ").strip().lower()
		
			if play_again != "yes":
					print("Game over. Goodbye!!")
					break
										
start_game()
