'''
Try to Find a Random Number Between 1-100 with Up and Down Expressions.(Right = 5)
** Search for 'python random' for 'random module'.
** Score out of 100. 20 Points per Question.
** Get the Rights Information from the User and Each Question Will Be Calculated Based on the Specified Number of Lives.
'''

import random

number = random.randint(1, 100)
right = int(input("Enter Number Of Life: "))
point = 100
life = right
while life > 0:
    print(f"**********************\nLife: {life}\n**********************")
    guess = int(input("Guess A Number: "))
    
    if guess == number:
        print(f"**********************\nCongratulations, You Know the Number.\nYour Point: {point}")
        break
    elif guess > number:
        print("**********************\nWrong guess.\nDown")
        life -= 1
        point -= (100 / right)
    else:
        print("**********************\nWrong guess.\nUp")
        life -= 1
        point -= (100 / right)

if life == 0:
    print("Your Life Is Over. Number:", number)