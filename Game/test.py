import os
from sys import exit
from random import randint
from textwrap import dedent
import numpy as np

class Reader(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def character_stats(self, character):
        file = open(self.file_name, 'r')
        stats_array = []
        for char in file:
            line = char.split()
            if line[0] == character:
                for i in range(len(line)):
                    if i == 0:
                        i += 1
                    elif i == 1:
                        continue
                    stat = int(line[i])
                    stats_array.append(stat)
                return stats_array

# test = Reader('character.txt')
# print(test.character_stats('Gnoll'))


class Battle(object):

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def x (self):
        print(self.enemy)

    load_stats = Reader('character.txt')
    player_stats = load_stats.character_stats(player)
    enemy_stats = load_stats.character_stats(enemy)

    if player_stats[5] > enemy_stats[5]:
        first_move = True
    else:
        first_move = False

    def randomizer(self, max):
        return random.randint(1, max)

    def dex_roll(self, dex):
        return dex + randomizer(20)

    def damage_calc(self):
        pass

    def turn(self, move):
        if move:
            attacker = self.player
            attacker_stats = self.player_stats
            defender = self.enemy
            defender_stats = self.enemy_stats
        else:
            attacker = self.enemy
            attacker_stats = self.enemy_stats
            defender = self.player
            defender_stats = self.player_stats
        return attacker, attacker_stats, defender, defender_stats
## attacker 0 - player attack enemy, 1 - reevers
## target_action 0  - dodge, 1 - def, 3- heal
    def attack(self, target_action):
        flag = True
        while self.player_stats[2] > 0 or self.enemy_stats[2] > 0:
            print(turn(flag).attacker_stats)
            turn(flag).attacker_stats[2] - 1
            if flag:
                flag = False
            else:
                flag = True
            # if dex_roll(self.attacker_stats[5]) < dex_roll(self.defender_stats[5]):
            #     print(f"{self.attacker} miss!")
            # else:
            #     if target_action = 0:



test = Battle('Sargarus', 'Gnoll')
# test.start_battle()
