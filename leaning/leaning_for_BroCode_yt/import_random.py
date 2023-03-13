# import random
""" 
import random

x = random.randint(1, 6)
y = random.random()

mylist = ['Rock', 'Paper', 'scissors']
#z = random.choice(mylist)
z = random.choices(mylist)

cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']

random.shuffle(cards)

print(z)
#print(cards) """

while True:
    import random
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors: ").lower()

    if player == computer:
        print("computer", computer)
        print("player", player)
        print("Tie!")
    elif player == "rock":
        if computer == 'paper':
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == 'scissors':
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
    elif player == "scissors":
        if computer == 'rock':
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == 'paper':
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
    elif player == "paper":
        if computer == 'scissors':
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == 'rock':
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
        
print("Bye!")

