# Program to develop  a single player rock_paper_scissor game  


import random


def stone_paper():
    player_score = 0
    computer_score = 0
    user_choice = ""
    num_of_play = 0
    while num_of_play < 3:
        user_choice = input("Pick from either of the following \n P for Paper \n S for Scissors \n R for Rock \n :").upper()
        if user_choice == "P":
            print("You chose Paper")
        elif user_choice == "R":
            print("You chose Rock")
        elif user_choice == "S":
            print("You chose Scissors")
        else:
            print("You entered a wrong letter")
        num_of_play = num_of_play + 1
        computer_list = ["R", "P", "S"]
        computer_choice = random.choice(computer_list)
        if user_choice == "R":
            if computer_choice == "S":
                print("You win. 1 score to you. Computer chose " + computer_choice + "\n")
                player_score = player_score + 1
            elif computer_choice == "P":
                print("Computer won. Computer chose " + computer_choice + "\n")
                computer_score = computer_score + 1
            else:
                print("There is a tie! computer has selected " + computer_choice + "\n")

        if user_choice == "S":
            if computer_choice == "P":
                print("You won. computer chose " + computer_choice + "\n")
                player_score += 1
            elif computer_choice == "R":
                print("Computer won. Computer chose " + computer_choice + "\n")
                computer_score += 1
            else:
                print("Its a tie!\n")

        if user_choice == "P":
            if computer_choice == "R":
                print("You win . Computer chose " + computer_choice + "\n")
                player_score += 1
            elif computer_choice == "S":
                print("Computer won. Computer chose " + computer_choice + "\n")
                computer_score += 1
            else:
                print("There's a tie  \n")

    if player_score > computer_score:
        print("Player won! " + str(player_score) + " out of " + str(num_of_play) + "games")
    elif player_score < computer_score:
        print("Computer won " + str(computer_score) + " out of " + str(num_of_play) + " games")
    else:
        print("Its a draw!")


print(stone_paper())