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

class Battle(object):

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        load_stats = Reader('character.txt')
        player_stats = load_stats.character_stats(player)
        enemy_stats = load_stats.character_stats(enemy)

        player_name = player_stats[0]
        player_HP = int(player_stats[1])
        player_STR = int(player_stats[2])
        player_DEF = int(player_stats[3])
        player_DEX = int(player_stats[4])

        enemy_name = enemy_stats[0]
        enemy_HP = int(enemy_stats[1])
        enemy_STR = int(enemy_stats[2])
        enemy_DEF = int(enemy_stats[3])
        enemy_DEX = int(enemy_stats[4])

        



class Save(object):
    def __init__(self, file_name):
        file = os.scandir('game/')

class Engine(object):

    def __init__(self, location_map):
        self.location_map = location_map

    def play(self):
        current_location = self.location_map.start_next_location()
        print(current_location)
        last_location = self.location_map.next_location_val('last_location')
        print(last_location)
        while current_location != last_location:
            next_loc_name = current_location.start_location()
            current_location = self.location_map.next_location_val(next_loc_name)
        current_location.start_location()

class Character(object):

    # def __init__(self, name, strength, health, dexterity):
    #     self.name = name
    #     self.strength = strength
    #     self.health = health
    #     self.dexterity = dexterity
    pass
class Player(Character):

    def __init__(self, arg):
        super(Player, self).__init__()

class Enemy(Character):

    def __init__(self, arg):
        super(Enemy, self).__init__()


class Locations(object):

    def start_location():
        print("Error!")
        exit(1)

class Death(Locations):
    def start_location():
        print("You are died!")
        exit(1)

class Loc11(Locations):
    def start_location(self):
        print("Goblin")
        return('1-2')

class Loc12(Locations):
    def start_location(self):
        print("2st Enemy")
        return('1-3')


class Loc13(Locations):
    def start_location(self):
        print("Boss_1")
        return('2-1')

class Loc21(Locations):
    def start_location(self):
        print("3st Enemy")
        return('2-2')

class Loc22(Locations):
    def start_location(self):
        print("3st Enemy")
        return('2-3')

class Loc23(Locations):
    def start_location(self):
        print("Boss_2")
        return('3-1')

class Loc31(Locations):
    def start_location(self):
        print("3st Enemy")
        return('3-2')

class Loc32(Locations):
    def start_location(self):
        print("Boss_3")
        return('3-3')

class Loc33(Locations):
    def start_location(self):
        print("3st Enemy")
        return('last_boss')

class LastBoss(Locations):
    def start_location(self):
        print("Boss")
        print(dedent("""
                Bug ugly troll stand before you and u can smell his rotten breath.
                It take some thime before he notice you and turn his head in your
                direction. Seems he studiyng you for some time and you almost can swear
                that for breef of moment you saw grimm smile on his face.
                While you draw your sword you notice giant pon on fire behind him and
                somting familiar in this pot. In next second you realise that is a
                humans foot and part of head. No time for hesitation, you ither will be
                a hero or snack for this creature.
                With a corner of you eyes you saw a swirt blink, you jump backward and
                was rly surprised by dexterity and speed of creature of this size. Time
                for final fight!
                """))
        return ('last_location')

class TheEnd(Locations):
    def start_location(self):
        print("Congrats, you beat the game!")
        exit(1)

class Map(object):

    locations = {
        '1-1':Loc11(),
        '1-2':Loc12(),
        '1-3':Loc13(),
        '2-1':Loc21(),
        '2-2':Loc22(),
        '2-3':Loc23(),
        '3-1':Loc31(),
        '3-2':Loc32(),
        '3-3':Loc33(),
        'last_boss':LastBoss(),
        'death':Death(),
        'last_location':TheEnd()

    }
    def __init__(self, next_location):
        self.next_location = next_location

    def next_location_val(self, location_name):
        loc = Map.locations.get(location_name)
        return loc
    def start_next_location(self):
        return self.next_location_val(self.next_location)


##runner
start = Map('1-1')
start_engine = Engine(start)
start_engine.play()
