import random

while True:
    user_a = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_a = random.choice(possible_actions)
    print(f"\nYou chose {user_a}, computer chose {computer_a}.\n")

    if user_a == computer_a:
        print(f"Both players selected {user_a}. It's a tie!")
    elif user_a == "rock":
        if computer_a == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_a == "paper":
        if computer_a == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_a == "scissors":
        if computer_a == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break