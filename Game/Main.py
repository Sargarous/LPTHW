class Save(object):

    def __init__(self, arg):
        super(Save, self).__init__()


class Character(object):
    pass

class Player(Character):

    def __init__(self, arg):
        super(Player, self).__init__()

class Enemy(Character):

    def __init__(self, arg):
        super(Enemy, self).__init__()

class Map(object):

    def __init__(self, arg):
        super(Map, self).__init__()

class Locations(object):

    def __init__(self, arg):
        super(Locations, self).__init__()
        self.arg = arg
