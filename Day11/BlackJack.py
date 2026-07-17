import random
from art import logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
def calculate_score(list_of_cards):
    sum_of_cards = sum(list_of_cards)
    if 11 in list_of_cards and 10 in list_of_cards and len(list_of_cards) == 2:
        return 0
    if 11 in list_of_cards and sum_of_cards > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
        sum_of_cards = sum(list_of_cards)
    return sum_of_cards
def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, Your score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input("Do you want to draw another card? (y/n): ")
            if choice == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
    while 0<computer_score<17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
while input("Do you want to play a game of Blackjack? (y/n): ") == "y":
    print("\n"*20)
    play_game()
