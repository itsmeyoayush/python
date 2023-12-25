import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def display_choices():
    print("Choose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        display_choices()

        user_choice = input("Enter your choice (1-3): ")
        
        if user_choice.lower() == 'quit':
            print("\nThanks for playing! Final Scores:")
            print(f"You: {user_score}  Computer: {computer_score}")
            break

        if user_choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter a number between 1 and 3 or type 'quit' to exit.")
            continue

        user_choice = int(user_choice)
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)

        print(f"\nYou chose {choices[user_choice-1]}")
        print(f"Computer chose {computer_choice}")

        result = determine_winner(choices[user_choice-1], computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"\nScores - You: {user_score}  Computer: {computer_score}")

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Type 'quit' at any time to exit.")

    while True:
        play_game()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()




