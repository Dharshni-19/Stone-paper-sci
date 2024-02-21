
import random

def play():
    user = get_user_choice()
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'Its a tie'


    if is_win(user, computer):
        return 'You won!'


    return 'You lost!'


def get_user_choice():
    while True:
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors \n")
        if user in ['r', 'p', 's']:
            return user
        else:
            print("Invalid choice. Please enter 'r', 'p', or 's'.")

def is_win(player, opponent):
    return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r')

if __name__ == "__main__":
    print(play())