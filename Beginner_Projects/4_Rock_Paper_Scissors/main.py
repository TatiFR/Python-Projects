rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# 0. Import random module 
import random

# 1. Ask for a number from person + Welcome text
print("Let's play a game of Rock, Paper, Scissors.")
selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. "))

# 2. Put the elements into a list and use index to pull the element chosen
elements = [rock, paper, scissors]
print(elements[selection])

# 3. Computer to generate random number (rock, paper, scissors)
computer_choice = random.randint(0, 2)
print("The computer's choice: \n" + elements[computer_choice])

# NOTE - element is integer, 
# 4. Depending on chosen element(person wins or loses to computer) - use if statements rock beats scissors, scissors beats paper, paper beats rock
if selection == computer_choice :
    print("It's a draw, try again.")
elif selection == 0 and computer_choice == 1:
    print("Paper beats Rock. You lose!")
elif selection == 1 and computer_choice == 2:
    print("Scissors beats Paper. You lose!")
elif selection == 2 and computer_choice == 0:
    print("Rock beats Scissors. You Lose!")
else: 
    print("You win!")
# 5. print results
