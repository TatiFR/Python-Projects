import random
from replit import clear()
from art import logo

def deal_card ():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards):
   """Take a list of cards and return the score calculated from the cards"""
   # return current_total
   if sum(cards) == 21 and len(cards) == 2: 
       return 0
   if 11 in cards and sum(cards) > 21:
       cards.remove(11)
       cards.append(1)
   return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack!"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You went over, you lose!"
    elif computer_score > 21:
        return "Opponent went over, you win!"
    elif user_score > computer_score:
        return "You win!"
    else: 
        return "You lose!"

def play_game():
    computers_cards = []
    users_cards = []
    is_game_over = False
    print(logo)
    
    for _ in range(2):
        users_cards.append(deal_card())
        computers_cards.append(deal_card())
    
    while not is_game_over: 
        user_score = calculate_score(users_cards)
        computer_score = calculate_score(computers_cards)

        if user_score == 0  or computer_score == 0 or user_score > 21:
            is_game_over = True
            # print(f"Your cards: {users_cards}, current score: {user_score}")
            # print(f"The computers cards: {computers_cards}, current score: {computer_score}") 
        else:
            user_should_deal = input("Do you want to draw a new card? Type 'Yes' or 'No': ")
            if user_should_deal == "Yes" or user_should_deal == "yes":
                users_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computers_cards.append(deal_card())
        computer_score = calculate_score(computers_cards)
    
    print(f" Your final hand: {users_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computers_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
