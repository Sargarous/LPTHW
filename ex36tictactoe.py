#just tic tac toe game
import time
import random
import numpy as np
from typing import List

field_rows = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
# field_rows = [['X', 'Z', '3'], ['C', 'H', 'P'], ['7', "1", '9']]

def randomizer(min, max):
    return random.randint(min, max)

def start():
    print("\t\tTic Tac Toe\n\t\t Menu:\n1.Player vs Player\n2.Player vs machine.")
    while True:
        mode_switcher = input('> ')
        if mode_switcher == '1':
            game_mode = 1
            print("PvP mode selected")
            break
        elif mode_switcher == '2':
            print("PvM")
            print("Choose your opponent: ")
            print("1. Io, herald of Jupiter.")
            print("2. Hellios, humiliator.")
            bot_switcher = input('> ')
            if bot_switcher == '1':
                print('Io is coming, you better be ready!')
                game_mode = 2
                break
            elif bot_switcher == '2':
                print('Hellios on the doorstep, prepeare your... things!')
                game_mode = 3
                break
            else:
                print("Don't be such a scaredy-cat, pick, come on!")
        else:
            print("Try again.")
    return(game_mode)

def playing_field_display():
    list_as_array = np.array(field_rows)
    print(list_as_array)

def pre_game_prep():
    print("Type Player 1 name: ")
    P1_name = input("> ")
    if game_mode == 1:
        print("Player 2: ")
        P2_name = input("> ")
        return (P1_name, P2_name)
    elif game_mode == 2:
        return(P1_name, "Io")
    else :
        return(P1_name, "Hellios")

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

def field_setter(matrix: List[List[str]], lst_value: str,
                  new_value: str) -> List:
    for sub_lst in field_rows:
        if lst_value in sub_lst:
            value_index = sub_lst.index(lst_value)
            sub_lst[value_index] = new_value
            return field_rows
    return field_rows

def victory_check(lst):
    winner = ''
    for i in range(0, 3):
        if (lst[i][0] == lst[i][1] and lst[i][0] == lst[i][2]):
            winner = lst[i][0]
    for j in range(0, 3):
        if (lst[0][j] == lst[1][j] and lst[0][j] == lst[2][j]):
            winner = lst[0][j]
    if (lst[0][0] == lst[1][1] and lst[0][0] == lst[2][2]):
        winner = lst[0][0]
    if (lst[0][2] == lst[1][1] and lst[0][2] == lst[2][0]):
        winner = lst[0][2]
    return winner


def gameplay(P1, P2, first_move):
    p1_sign = 'X'
    p2_sign = 'O'
    p1 = P1
    p2 = P2
    p1_turn = True
    if first_move == P2:
        p1 = P2
        p2 = P1
        p1_turn = False
    playing_field_display()
    for i in range(0, 9):
            if i%2 == 0:
                if(p1 == 'Io' or p1 == 'Hellios'):
                    position = io_bot(field_rows)
                    print(f"{p1} strike on {position}")
                else:
                    print(f"{p1}, type number of field where you want to set {p1_sign}")
                    position = input("> ")
                field_setter(field_rows, position, p1_sign)
                playing_field_display()
            else:
                if(p2 == 'Io' or p2 == 'Hellios'):
                    position = io_bot(field_rows)
                    print(f"{p1} strike on {position}")
                else:
                    print(f"{p2}, type number of field where you want to set {p2_sign}")
                    position = input("> ")
                field_setter(field_rows, position, p2_sign)
                playing_field_display()
            winner = victory_check(field_rows)
            if  winner == p1_sign:
                print(f"Congrts, {p1} is winner of this match!")
                print(f"Sad for you, mr.{p2}")
                break
            elif winner == p2_sign:
                print(f"Congrts, {p2} is winner of this match!")
                print(f"Sad for you, mr.{p1}")
                break


def io_bot(field_rows):
    while True:
        io_turn = str(randomizer(1, 9))
        for row in field_rows:
            for val in row:
                if (val == io_turn):
                    return io_turn
def io_bot(field_rows):
    while True:
        hellios_turn = str(randomizer(1, 9))
        for row in field_rows:
            for val in row:
                if (val == hellios_turn):
                    return hellios_turn


# print(io_bot(field_rows))

game_mode = start()
P1, P2 = pre_game_prep()
first_move = who_move_first()
gameplay(P1, P2, first_move)
