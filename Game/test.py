import os
from sys import exit
from random import randint
from textwrap import dedent

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

test = Reader('character.txt')
print(test.character_stats('Gnoll'))
class Battle(object):

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    load_stats = Reader('character.txt')
    player_stats = load_stats.character_stats(player)
    enemy_stats = load_stats.character_stats(enemy)

    def randomizer(max):
        return random.randint(1, max)

## attacker 0 - player attack enemy, 1 - enemy
    def attack(self, player_stats, enemy_stats, attacker):
        if attacker == 0:
            if passenemy_stats[5] + randomizer(20) > player_stats[4] + randomizer(20):
                print(f"{self.player} miss!")

test = Battle('Sargarus', 'Gnoll')
test.start_battle()
