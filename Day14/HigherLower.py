from art import *
import random
from game_data import *
def comparison(dummy_score,dummy_a,dummy_b,dummy_list):
    followers = input("Who has more followers? Type 'A' or 'B': ").lower()
    exclude1 = dummy_a
    exclude2 = dummy_b
    if followers == "a" and dummy_a["follower_count"] > dummy_b["follower_count"]:
        dummy_score += 1
        dummy_list.remove(dummy_b)
        dummy_b = random.choice([x for x in dummy_list if x != exclude1])
    elif followers == "b" and dummy_b["follower_count"] > dummy_a["follower_count"]:
        dummy_list.remove(dummy_a)
        dummy_a = dummy_b
        dummy_b = random.choice([x for x in dummy_list if x != exclude2])
        dummy_score += 1
    else:
        print("\n"*30)
        print(logo)
        print(f"Sorry that's wrong. Final score: {dummy_score}")
        return
    print("\n"*30)
    game(dummy_score,dummy_a,dummy_b)
def game(score,a,b):
    print(logo)
    if a["follower_count"] >= b["follower_count"]:
        print("Its A")
    elif b["follower_count"] > a["follower_count"]:
        print("Its B")
    if len(data) > 1:
        if score > 0:
            print(f"You are Right! Current Score: {score}")
        print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")
        print(vs)
        print(f"Against B: {b["name"]}, a {b["description"]}, from {b["country"]}")
        comparison(score,a,b,data)
    else:
        print(f"All your answer were correct! You Won! Final score: {score}")
        print(win)
        return
actual_a = random.choice(data)
actual_b = random.choice(data)
actual_score = 0
while actual_a == actual_b:
    actual_b = random.choice(data)
game(actual_score,actual_a,actual_b)
