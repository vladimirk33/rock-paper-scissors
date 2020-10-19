import random

MOVES = ("rock", "paper", "scissors")
WINS = (("paper", "rock"),
        ("scissors", "paper"),
        ("rock", "scissors"))
LOSES = (("rock", "paper"),
         ("paper", "scissors"),
         ("scissors", "rock"))


def human_move():
    user_move = input()
    return user_move


def computer_move():
    ai_move = random.choice(MOVES)
    return ai_move


def choose_winner(human_move, computer_move):
    for human, computer in WINS:
        if human_move == human and computer_move == computer:
            print(f"Well done. The computer chose {computer_move} and failed")
    for human, computer in LOSES:
        if human_move == human and computer_move == computer:
            print(f"Sorry, but the computer chose {computer_move}")
    if human_move == computer_move:
        print(f"There is a draw ({computer_move})")


def main():
    human = human_move()
    computer = computer_move()
    choose_winner(human, computer)


if __name__ == "__main__":
    main()
