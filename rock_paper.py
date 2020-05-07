# Program to develop a rock,paper,scissor game between the computer & a user using numbers

import random


def rock_paper():
    player_1 = 0
    player_2 = 0
    scissors = 0
    n = 0

    def int_check(intnum):
        while True:
            try:
                user = int(input(intnum))
            except ValueError:
                print("You did not enter a number")
                continue
            else:
                return user

    user = ""
    while user != scissors and n <= 3:
        user = int_check("Enter the number between 0 and 5 you want the system to guess :\n")

        scissors = random.randint(0, 5)
        if scissors < user:
            print("the system guess was low " + str(scissors))
            player_1 += 1
        elif scissors > user:
            print("The system guess was high " + str(scissors))
            player_1 += 1
        n = n + 1
    if scissors == user:
        print("You lost! Computer guessed right! ")
        player_2 += 1
    else:
        print("You won. Play again!")
    if player_1 > player_2:
        print("your score " + str(player_1) + " out of " + str(n) + " games")
    elif player_1 < player_2:
        print("You loose " + str(player_2) + " out of" + str(n) + " games")


print(rock_paper())
