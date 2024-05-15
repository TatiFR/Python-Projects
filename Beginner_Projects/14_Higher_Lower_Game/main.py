# 1 import the art and data
from multiprocessing.connection import answer_challenge
from art import logo
from art import vs
from game_data import data
import random

SCORE = 0
continue_game = True

# If it is a new game both options are new but if continuing a game, option a must be the answer from previous choice
# 2 Check if answer is correct
def check_answer(guess, answer):
    global SCORE
    global continue_game
    """checks answer against guess. If right, game continues otherwise game over."""
    if guess == answer:
        SCORE += 1
        print(f"You're right! Current score: {SCORE}")
    else:
        continue_game = False
        print(f"Sorry that's wrong! Final score: {SCORE}")
# 3 Keep score of the number of times player has answered correctly

# 4 Wrong answer def, clear screen print loosing message

# FINAL join all the steps to run the game
def game():
    print(logo)
    # 2 Have a comparison which will give the player two options, calling the followers from game_data
    if SCORE == 0:
        option_a = random.choice(data)
        option_b = random.choice(data)

    else: 
        if answer == "B":
            option_a = option_b 
        option_b = random.choice(data)
    a = int(option_a['follower_count'])
    b = int(option_b['follower_count'])   
    if a < b: 
        answer = "B"
    else:
        answer = "A"
    print(f"Compare A: {option_a['name']}, {option_a['description']}, {option_a['country']}")
    print(vs)
    print(f"Compare B: {option_b['name']}, {option_b['description']}, {option_b['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ")
    check_answer(guess, answer)
    

while continue_game: 
    game()
