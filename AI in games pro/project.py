import random
def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_input in choices:
            return user_input
        print("Invalid choice. Please try again.")
def get_ai_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(user, ai):
    if user == ai:
        return "It's a tie!"
    if (user == 'rock' and ai == 'scissors') or \
       (user == 'scissors' and ai == 'paper') or \
       (user == 'paper' and ai == 'rock'):
        return "You win!"
    return "AI wins!"
def play():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        ai_choice = get_ai_choice()
        print(f"You chose: {user_choice}")
        print(f"AI chose: {ai_choice}")
        result = determine_winner(user_choice, ai_choice)
        print(result)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
if __name__ == "__main__":
    play()
