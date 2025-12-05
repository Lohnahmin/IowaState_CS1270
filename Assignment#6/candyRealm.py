# Lyle Osburne
# 12/01/2025
# Assignment #6 - Candy Realm
# Candy Land style game where up to four players (human and/or computer) move along a candy-themed track by drawing cards.

import random

BOARD = [
    "START",
    "M", "R", "B", "M", "C", "G", "B", "Y",
    "C", "B", "G", "Y", "G", "C", "Y", "R", "M", "R",
    "GOAL"
]

COLORS = ["M", "R", "B", "C", "G", "Y"]


def show_header():
    print("Candy Realm!")
    print("By: Your Name")
    print("[COM S 127 1]")
    print("-" * 65)


def get_int_in_range(prompt, low, high):
    while True:
        text = input(prompt)
        try:
            value = int(text)
            if low <= value <= high:
                return value
            else:
                print(f"Please enter a whole number between {low} and {high}.")
        except ValueError:
            print("That input is not a valid integer. Try again.")


def show_instructions():
    print()
    print("=== HOW TO PLAY CANDY REALM ===")
    print("Up to four players race along a candy-themed path.")
    print("Each turn, a card is drawn that shows a color like R, B, G, Y, M, or C.")
    print("The player moves forward to the next space on the board that matches")
    print("that color. If there is no later space with that color, they jump to GOAL.")
    print()
    print("Human players can:")
    print("  d - draw the next card and move")
    print("  s - shuffle the deck instead of moving")
    print("  q - end the current game and go back to the main menu")
    print()
    print("Computer players choose randomly between drawing and shuffling.")
    print("The first player to land on the GOAL space wins the game.")
    print()
    input("Press Enter to go back to the main menu...")
    print()


def build_deck(copies_per_color):
    deck = []
    for c in COLORS:
        for _ in range(copies_per_color):
            deck.append(c)
    random.shuffle(deck)
    return deck


def create_players(num_humans):
    players = []
    for i in range(4):
        player_num = i + 1
        if player_num <= num_humans:
            ptype = "HUMAN"
        else:
            ptype = "COMPUTER"
        players.append({
            "name": f"Player {player_num}",
            "type": ptype,
            "pos": 0
        })
    return players


def display_board(board, players, deck):
    print(" 1")
    print(" 2")
    print(" 3")
    print(" 4")

    print(" TRACK", end=" ")
    print("START", end=" ")
    for space in board[1:-1]:
        print(space, end=" ")
    print("GOAL")

    print(" DECK ", end=" ")
    for card in deck:
        print(card, end=" ")
    print()

    markers = []
    for idx, space in enumerate(board):
        here = []
        for p in players:
            if p["pos"] == idx:
                here.append(p["name"][-1])
        if not here:
            markers.append(".")
        else:
            markers.append("".join(here))

    print(" PLYRS ", end="")
    for token in markers[1:-1]:
        print(token, end=" ")
    print()
    print()


def move_player_for_card(player, card, board):
    current_pos = player["pos"]
    moved = 0
    for i in range(current_pos + 1, len(board)):
        if board[i] == card:
            player["pos"] = i
            moved = i - current_pos
            return moved

    player["pos"] = len(board) - 1
    moved = (len(board) - 1) - current_pos
    return moved


def human_turn(player, deck, board, copies_per_color):
    while True:
        if not deck:
            print("The deck ran out, building and shuffling a fresh one...")
            deck.extend(build_deck(copies_per_color))
        top_card = deck[0]
        prompt = (
            f"{player['name']} ({player['type']}), choose an action "
            f"[d = draw {top_card}, s = shuffle, q = quit]: "
        )
        choice = input(prompt).strip().lower()
        if choice == "d":
            card = deck.pop(0)
            moved = move_player_for_card(player, card, board)
            print(f"{player['name']} ({player['type']}) drew: {card}")
            print(f"{player['name']} now moves ahead by {moved} space(s).")
            input("Press Enter to continue...")
            return "ok"
        elif choice == "s":
            random.shuffle(deck)
            print(f"{player['name']} ({player['type']}) shuffled the deck.")
            input("Press Enter to continue...")
            return "ok"
        elif choice == "q":
            print(f"{player['name']} ended the game early.")
            input("Press Enter to return to the main menu...")
            return "quit"
        else:
            print("Please type d, s, or q.")


def computer_turn(player, deck, board, copies_per_color):
    if not deck:
        deck.extend(build_deck(copies_per_color))

    action = random.choice(["draw", "draw", "draw", "shuffle"])

    if action == "shuffle" and len(deck) > 1:
        random.shuffle(deck)
        print(f"{player['name']} ({player['type']}) decided to shuffle the deck.")
        input("Press Enter to continue...")
    else:
        card = deck.pop(0)
        moved = move_player_for_card(player, card, board)
        print(f"{player['name']} ({player['type']}) drew: {card}")
        print(f"{player['name']} moves forward {moved} space(s).")
        input("Press Enter to continue...")


def play_game():
    print()
    num_humans = get_int_in_range(
        "Enter how many human players are playing (1-4): ", 1, 4
    )
    copies = get_int_in_range(
        "Enter how many copies of each color card to use (1-5): ", 1, 5
    )
    print()

    board = BOARD[:]
    players = create_players(num_humans)
    deck = build_deck(copies)

    winner = None
    quit_flag = False

    while not winner and not quit_flag:
        display_board(board, players, deck)
        for player in players:
            if player["type"] == "HUMAN":
                result = human_turn(player, deck, board, copies)
                if result == "quit":
                    quit_flag = True
                    break
            else:
                computer_turn(player, deck, board, copies)

            if player["pos"] == len(board) - 1:
                winner = player
                break

        if not deck and not quit_flag and not winner:
            deck = build_deck(copies)

    if winner and not quit_flag:
        print()
        print(f"{winner['name']} ({winner['type']}) reached the GOAL and wins the race!")
        print()
        input("Press Enter to go back to the main menu...")
    print()


def main_menu():
    while True:
        choice = input("MAIN MENU - [p]lay, [i]nstructions, [q]uit: ").strip().lower()
        if choice == "p":
            play_game()
        elif choice == "i":
            show_instructions()
        elif choice == "q":
            print("Exiting Candy Realm. Thanks for playing.")
            break
        else:
            print("That option was not recognized. Please enter p, i, or q.")


def main():
    show_header()
    main_menu()


if __name__ == "__main__":
    main()
