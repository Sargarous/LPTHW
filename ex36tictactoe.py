#just tic tac toe game
import time
import random
import numpy as np
from typing import List

# field_rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
field_rows = [['X', 'X', 'X'], [4, 5, 6], [7, 8, 9]]

def randomizer(min, max):
    return random.randint(min, max)

def start(game_mode):
    print("\t\tTic Tac Toe\n\t\t Menu:\n1.Player vs Player\n2.Player vs machine.")
    print(f"game_mode = {game_mode}")
    while True:
        mode_switcher = input('> ')
        if "1" in mode_switcher:
            game_mode = 1
            print("PvP mode selected")
            break
        elif "2" in mode_switcher:
            game_mode = 2
            print("PvM")
            break
        else:
            print("Try again.")
    return(game_mode)

def playing_field_display():
    list_as_array = np.array(field_rows)
    print(list_as_array)

def pre_game_prep():
    print("Type Player 1 name: ")
    P1_name = input("> ")
    print("Player 2: ")
    P2_name = input("> ")
    return (P1_name, P2_name)

def who_move_first():
    print("First goes: ")
    progress_bar()
    if randomizer(0, 1) == 0:
        first = P1
        print(P1)
    else:
        first = P2
        print(P2)
    return (first)

def progress_bar():
    i = 0
    while i < 10:
        time.sleep(randomizer(0, 1))
        print("-", sep = ' ', end = '', flush = True)
        i += 1

def field_setter(matrix: List[List[int]], lst_value: int,
                  new_value: int) -> List:
    for sub_lst in field_rows:
        if lst_value in sub_lst:
            value_index = sub_lst.index(lst_value)
            sub_lst[value_index] = new_value
            return field_rows
    return field_rows


def all_same(line_of_field):
    if all(x == line_of_field for x in line_of_field):
        print(all(x == line_of_field[0] for x in line_of_field))
        print (line_of_field)
        if 'X' in line_of_field:
            return 'X'
        elif 'O' in line_of_field:
            return 'O'
    print(line_of_field)
# all_same(field_rows[2])
def victory_check():

    for i in range(0, 3):
        print(i)
        check1 = [row[i] for row in field_rows]
        all_same(check1)
        # print(f"check1 {check1 == 'X' or 'O'}")
        check2 = all_same([field_rows[i]])
        # print(f"check2 {check2 == 'X' or 'O'}")

        # print([row[i] for row in field_rows])
        # print(field_rows[i])
        if check1 == 'X' or 'O':
            return check1
        elif check2 == 'X' or 'O':
            return check2

    # check = all_same([field_rows[0][0], field_rows[1][1], field_rows[2][2]])
    # if check == 'X' or 'O':
    #     return check
    # check = all_same([field_rows[0][2], field_rows[1][1], field_rows[2][0]])
    # if check == 'X' or 'O':
    #     return check

# playing_field_display()
#
print(f"Vi_check_res {victory_check()}")


def gameplay(P1, P2, first_move):
    player_turn = 0
    p1_sign = 'X'
    p2_sign = 'O'
    p1 = P1
    p2 = P2
    if first_move == P2:
        p1 = P2
        p2 = P1
    playing_field_display()
    for i in range(0, 3):
        if i%2 == 0:
            print(f"{p1}, type number of field where you want to set {p1_sign}")
            position = input("> ")
            field_setter(field_rows, int(position), p1_sign)
            playing_field_display()
            player_turn += 1
        else:
            print(f"{p2}, type number of field where you want to set {p2_sign}")
            position = input("> ")
            field_setter(field_rows, int(position), p2_sign)
            playing_field_display()
            player_turn += 1



# game_mode = start(0)
# P1, P2 = pre_game_prep()
# first_move = who_move_first()
# gameplay(P1, P2, first_move)
# field_setter()
# field_setter(field_rows, 8, 'X')


# playing_field_display()
