import random

GAME_CASES = {}
WINNING_CASES = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
    'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],
    'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
    'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
    'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
    'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
    'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
    'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
    'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
    'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
    'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
    'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
}


def choose_option(option):
    if option == '':
        GAME_CASES['rock'] = WINNING_CASES['rock']
        GAME_CASES['paper'] = WINNING_CASES['paper']
        GAME_CASES['scissors'] = WINNING_CASES['scissors']
        return GAME_CASES
    else:
        option_list = option.split(",")
        for option in option_list:
            if option in WINNING_CASES:
                GAME_CASES[option] = WINNING_CASES[option]


def read_player_score(name):
    try:
        file = open("rating.txt", "r+", encoding="utf-8")
    except (FileExistsError, FileNotFoundError):
        file = open("rating.txt", "w+", encoding="utf-8")
    for player in file.readlines():
        player = player.split()
        if player[0] == name:
            file.close()
            return player[1]
    file.write(f"{name} 0\n")
    file.close()


def write_player_score(name, mode):
    reading_file = open("rating.txt", "r")
    new_file_content = ""
    for line in reading_file:
        stripped_line = line.strip()
        player = stripped_line.split()
        if player[0] == name:
            delta = 0
            if mode == "win":
                delta = 100
            elif mode == "tie":
                delta = 50
            new_line = stripped_line.replace(f"{player[0]} {player[1]}",
                                             f"{player[0]} {int(player[1]) + delta}")
        else:
            new_line = stripped_line
        new_file_content += new_line + "\n"
    reading_file.close()

    writing_file = open("rating.txt", "w")
    writing_file.write(new_file_content)
    writing_file.close()


def human_move():
    user_move = input()
    while user_move not in GAME_CASES.keys() \
            and user_move not in ("!rating", "!exit"):
        print("Invalid input")
        user_move = input()
    return user_move


def computer_move():
    ai_move = random.choice(list(GAME_CASES.keys()))
    return ai_move


def choose_winner(human_move, computer_move, name):
    if computer_move in GAME_CASES[human_move]:
        print(f"Well done. The computer chose {computer_move} and failed")
        mode = "win"
        write_player_score(name, mode)
    elif human_move == computer_move:
        print(f"There is a draw ({computer_move})")
        mode = "tie"
        write_player_score(name, mode)
    else:
        print(f"Sorry, but the computer chose {computer_move}")


def main():
    name = input("Enter your name: ")
    print("Hello,", name)
    read_player_score(name)
    print("Choose the mode: ")
    for item in list(WINNING_CASES.keys()):
        print(f"- {item}")
    print("Separate by comma. Example: gun,devil,dragon")
    choose_option(input("> "))
    print("Write \"!rating\" to look your score.")
    print("Write \"!exit\" to quit the game.")
    print("Okay, let's start")
    while True:
        human = human_move()
        if human == "!rating":
            print("Your rating:", read_player_score(name))
            continue
        elif human == "!exit":
            break
        computer = computer_move()
        choose_winner(human, computer, name)
    print("\nBye!")


if __name__ == "__main__":
    main()
