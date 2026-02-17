import random
from art import rock, paper, scissors

print("Welcome to Rock Paper Scissors!")
while True:
    user_moves =int(input("what do you choose?Type 0 for Rock,1 for Paper or 2 for Scissors: "))
    
    game_moves=[rock,paper,scissors]
    computer_moves = random.choice(game_moves)
    
    if user_moves >=0 and user_moves <=2:
        print(game_moves[user_moves])
        print("Computer Choose")
        print(computer_moves)
    
    if user_moves < 0 or user_moves > 2:
        print("you typed invalid number,You Lose!")
    elif computer_moves == rock and user_moves == 2:
        print("You Lose!")
    elif computer_moves == scissors and user_moves == 0:
        print("You Win!")
    elif computer_moves == paper and user_moves == 2:
        print("You Win!")
    elif computer_moves == scissors and user_moves == 1:
        print("You Lose!")
    elif computer_moves == rock and user_moves == 1:
        print("You Win!")
    elif computer_moves == paper and user_moves == 0:
        print("You Lose!")
    else:
        print("It's a draw!")
        
    next_round = input("Do you want to play again?Type yes or no: ").lower()
    if next_round == "yes":
        continue
    else:
        break