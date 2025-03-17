import random
import art
repeat='y'
while repeat=='y':
    print(art.logo)


    print("welcome to the number guessing game!")
    num=random.randint(1,100)
    print("I am thinking of a number between 1 and 100")
    difficulty=input("Choose Difficulty level type 'easy' or 'hard': ")
    if difficulty.lower()=='easy':
        attempt=10
    elif difficulty.lower()=='hard':
        attempt=5
    def guess(attempt):
        
        for i in range(attempt):
            guess=int(input("Make a guess: "))
                    
            if guess>num:
                print(f"Too high.\nGuess again\nYou have {attempt-(i+1)} left ")
            elif guess<num:
                print(f"Too low.\nGuess again\nYou have {attempt-(i+1)} left")
            elif guess==num :
                print(f"You got it! The number is {guess}")
                repeat = input("if you need to continue game, Type 'y' ")
                break
            if i==attempt-1:
                print(f"You lose.\nThe number is {num}")
                repeat = input("if you need to continue game, Type 'y' ")

    guess(attempt)   
        



