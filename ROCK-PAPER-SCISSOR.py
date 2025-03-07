import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

def get_winner(user, computer):
    global user_score, computer_score
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = get_winner(user_choice, computer_choice)
    print(result)
    print(f"Score - You: {user_score} | Computer: {computer_score}")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
