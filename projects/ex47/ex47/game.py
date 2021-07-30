class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        dir = self.paths.get(direction, None)
        print(f"we go in {dir} dir")
        return dir

    def add_paths(self, paths):
        self.paths.update(paths)
