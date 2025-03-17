import random

cards=[2,3,4,5,6,7,8,9,10,10,10,10,11]


p1=random.choices(cards,k=5)

p2=random.choices(cards,k=5)
player=[random.choice(cards)]
computer=[]
for i in range(len(p1)):
    
    player.append(p1[i])
    
    computer.append(p2[i])
    if sum(player) > 21:
        

        print(f"Your cards are: {player} and sum is {sum(player)}\nYou exceeded the 21")
        
        print("Bust!")
        break
    


    print(f"Your cards are: {player} and sum is {sum(player)}\ncomputer cards are: {computer} and sum is {sum(computer)}")
    choice=input("type 'y' to pick one more card or 'n' to complete the game: ")
    
    if choice.lower()=='n':
        if sum(computer)>sum(player):
            print("Computer wins!")
            break
        elif sum(computer)<sum(player):
            print("You win!")
            break
        else:
            print("It's a tie!")
            break

                   



