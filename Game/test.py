import os
from sys import exit
from random import randint
from textwrap import dedent

class Reader(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def character_stats(self, character):
        file = open(self.file_name, 'r')
        for char in file:
            line = char.split()
            if line[0] == character:
                return line

# test = Reader('character.txt')
# print(test.character_stats('Gnoll'))
class Battle(object):

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        load_stats = Reader('character.txt')
        player_stats = load_stats.character_stats(self.player)
        # enemy_stats = load_stats.character_stats(enemy)
        player_name = player_stats[0]
        player_HP = int(player_stats[1])
        player_STR = int(player_stats[2])
        player_DEF = int(player_stats[3])
        player_DEX = int(player_stats[4])
        print(player_name, player_HP, player_STR, player_DEF, player_DEX)
        print(self.enemy)
        print(player_HP - player_STR)

test = Battle('Sargarus', 'Gnoll')
test.start_battle()
