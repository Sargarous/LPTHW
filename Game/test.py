import os
import time
from sys import exit
import random
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

    def randomizer(self, max):
        return random.randint(3, max)

    def progress_bar(self):
        for i in range (0, 8):
            time.sleep(random.uniform(0.1, 0.6))
            print("-", sep = ' ', end = '', flush = True)
## attacker 0 - player attack enemy, 1 - reevers
## target_action 0  - dodge, 1 - def, 3- heal
    def attack(self):
        move = False
        load_stats = Reader('character.txt')
        player_stats = load_stats.character_stats(self.player)
        enemy_stats = load_stats.character_stats(self.enemy)
        if player_stats[3] > enemy_stats[3]:
            move = True
        while True:
            if move:
                attacker = self.player
                attacker_stats = player_stats

                defender = self.enemy
                defender_stats = enemy_stats

                print(f"{attacker} attack {defender}")
                print(f"{defender} health: {defender_stats[0]}")
                self.progress_bar()
                print('\n')
                if self.randomizer(attacker_stats[3] * 2) < self.randomizer(defender_stats[3]):
                    print(f"{defender} dodge strike from {attacker}.\n")
                else:
                    damage = attacker_stats[1] + self.randomizer(attacker_stats[3]) - defender_stats[2]
                    defender_stats[0] = defender_stats[0] - damage
                    print(f"{attacker} hit {defender} with the sword, {defender} lost {damage} health.")
                    print(f"{defender} HP: {defender_stats[0]}\n")

            else:
                attacker = self.enemy
                attacker_stats = enemy_stats

                defender = self.player
                defender_stats = player_stats

                print(f"{attacker} attack {defender}")
                self.progress_bar()
                print('\n')
                if self.randomizer(attacker_stats[3] * 2) < self.randomizer(defender_stats[3]):
                    print(f"{defender} dodge strike {attacker}.\n")
                else:
                    damage = attacker_stats[1] + self.randomizer(attacker_stats[3]) - defender_stats[2]
                    defender_stats[0] = defender_stats[0] - damage
                    print(f"{attacker} hit {defender} with the sword, {defender} lost {damage} health.")
                    print(f"{defender} HP: {defender_stats[0]}\n")

            if move:
                move = False
            else:
                move = True

            if player_stats[0] <= 0 or enemy_stats[0] <= 0:
                print(f"{attacker} win!")
                break
            # if dex_roll(self.attacker_stats[5]) < dex_roll(self.defender_stats[5]):
            #     print(f"{self.attacker} miss!")
            # else:
            #     if target_action = 0:



test = Battle('Sargarus', 'Gnoll')
test.attack()
