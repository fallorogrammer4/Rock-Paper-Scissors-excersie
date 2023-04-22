import random

user_wins = 0
cpu_wins = 0

options = [ "rock", "papper", "scissors"]


while True:
    us_input = input("Type Rock/Papper/Scissors or Q to quit " ).lower()

    if us_input == "q":
        break

    if us_input  not  in options:
        continue

    random_number = random.randint(0, 2)
   # rock = 0
   #paper = 1
   # scissors = 2
    cpu_pick = options[random_number]
    print( "Computer picked", cpu_pick + ".")

       #Picking winner
    if us_input == "rock" and cpu_pick == "scissors":
       print("You won :)")
       user_wins += 1
    elif us_input == "papper" and cpu_pick == "rock":
       print("You won :) ")
       user_wins += 1
    elif us_input == "scissors" and cpu_pick == "papper":
       print("You won :)")
       user_wins += 1
    elif us_input == "papper" and cpu_pick == "papper":
       print("Draw :| ")
       user_wins += 0
     elif us_input == "scissors" and cpu_pick == "scissors":
       print("Draw :| ")
       user_wins += 0
        elif us_input == "rock" and cpu_pick == "rock":
       print("Draw :| ")
       user_wins += 0

    else:
           print("You lost :(")
           cpu_wins += 1

print("You won",  user_wins, "times")
print("Computer wins", cpu_wins, "times")
print("Bye Bye")
