#just tic tac toe game
import time
import random
import numpy as np
from typing import List

field_rows = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
# field_rows = [['X', 'Z', '3'], ['2', 'X', 'P'], ['7', "1", '9']]
#return random number in range(z, y)
def randomizer(min, max):
    return random.randint(min, max)

#game mode selector(PvP or PvMachine)
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

#draw game field in com.line
def playing_field_display():
    list_as_array = np.array(field_rows)
    print(list_as_array)
#player name input
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
#first move coin flip
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
#fancy stuff
def progress_bar():
    for i in range (0, 11):
        time.sleep(randomizer(0, 1))
        print("-", sep = ' ', end = '', flush = True)

#set O or X in selected position(1-9)
def field_setter(matrix: List[List[str]], lst_value: str,
                  new_value: str) -> List:
    for sub_lst in field_rows:
        if lst_value in sub_lst:
            value_index = sub_lst.index(lst_value)
            sub_lst[value_index] = new_value
            return field_rows
    return field_rows
#check field for 3-in-a-row
def victory_check(lst):
    winner = ''
    for i in range(0, 3):
        if (lst[i][0] == lst[i][1] and lst[i][0] == lst[i][2]):
            return lst[i][0]
    for j in range(0, 3):
        if (lst[0][j] == lst[1][j] and lst[0][j] == lst[2][j]):
            return lst[0][j]
    if (lst[0][0] == lst[1][1] and lst[0][0] == lst[2][2]):
        return lst[0][0]
    if (lst[0][2] == lst[1][1] and lst[0][2] == lst[2][0]):
        return lst[0][2]
    return winner

#main method, assemble values and queue players turns
def gameplay(P1, P2, first_move):
    p1_sign = 'X'
    p2_sign = 'O'
    p1 = P1
    p2 = P2
    if first_move == P2:
        p1 = P2
        p2 = P1
    playing_field_display()
    for i in range(0, 9):
            if i%2 == 0:
                if(p1 == 'Io' or p1 == 'Hellios'):
                    position = bot_activator()
                    print(f"{p1} strikes {p1_sign} on {position}")
                else:
                    print(f"{p1}, type number of field where you want to set {p1_sign}")
                    position = input("> ")
                field_setter(field_rows, position, p1_sign)
                playing_field_display()
            else:
                if(p2 == 'Io' or p2 == 'Hellios'):
                    position = bot_activator()
                    print(f"{p1} strikes {p1_sign} on {position}")
                else:
                    print(f"{p2}, type number of field where you want to set {p2_sign}")
                    position = input("> ")
                field_setter(field_rows, position, p2_sign)
                playing_field_display()
            winner = victory_check(field_rows)
            if  winner == p1_sign:
                print(f"Congrats, {p1} is winner of this match!")
                print(f"Sad for you, mr.{p2}")
                break
            elif winner == p2_sign:
                print(f"Congrats, {p2} is winner of this match!")
                print(f"Sad for you, mr.{p1}")
                break
            elif not winner and i == 8:
                print("Draw!")

#use a different script depending on the selected difficulty
def bot_activator():
    if game_mode == 2:
        return io_bot(field_rows)
    elif game_mode == 3:
        return Hellios_bot(field_rows)

#simple randomized action bot
def io_bot(field_rows):
    while True:
        io_turn = str(randomizer(1, 9))
        for row in field_rows:
            for val in row:
                if (val == io_turn):
                    return io_turn

#advanced bot, smart as hell, sharp as edge, stings like a bee and etc.
def Hellios_bot(field_rows):
    hellios_turn = win_turn_avaible(field_rows)
    if hellios_turn:
        return hellios_turn
    else:
        while True:
            hellios_turn = str(randomizer(1, 9))
            for row in field_rows:
                for val in row:
                    if (val == hellios_turn):
                        return hellios_turn

#check for two same and empty third
def win_turn_avaible(lst):
#horizon check
    for i in range(0, 3):
        if (lst[i][0] == lst[i][1] and lst[i][2] != 'X' and lst[i][2] != 'O'):
            return lst[i][2]
        elif (lst[i][2] == lst[i][1] and lst[i][0] != 'X' and lst[i][0] != 'O'):
            return lst[i][0]
    #horrizon opposit check x 2 x
        elif (lst[i][0] == lst[i][2] and lst[i][1] != 'X' and lst[i][2] != 'O'):
            return lst[i][1]
#vertical check
    for j in range(0, 3):
        if (lst[0][j] == lst[1][j] and lst[2][j] != 'X' and lst[2][j] != 'O'):
            return lst[2][j]
        elif (lst[1][j] == lst[2][j] and lst[0][j] != 'X' and lst[0][j] != 'O'):
            return lst[0][j]
    #vertical opposit check
        elif (lst[0][j] == lst[2][j] and lst[1][j] != 'X' and lst[1][j] != 'O'):
            return lst[1][j]
#diagonal left up start check
    if (lst[0][0] == lst[1][1] and lst[2][2] != 'X' and lst[2][2] != 'O'):
        return lst[2][2]
    elif (lst[1][1] == lst[2][2] and lst[0][0] != 'X' and lst[0][0] != 'O'):
        return lst[0][0]
    elif (lst[0][0] == lst[2][2] and lst[1][1] != 'X' and lst[1][1] != 'O'):
        return lst[1][1]
#diag right up start
    if (lst[0][2] == lst[1][1] and lst[2][0] != 'X' and lst[2][0] != 'O'):
        return lst[2][0]
    elif (lst[2][0] == lst[1][1] and lst[0][2] != 'X' and lst[0][2] != 'O'):
        return lst[0][2]
    elif (lst[2][0] == lst[0][2] and lst[1][1] != 'X' and lst[1][1] != 'O'):
        return lst[1][1]


game_mode = start()
P1, P2 = pre_game_prep()
first_move = who_move_first()
gameplay(P1, P2, first_move)
