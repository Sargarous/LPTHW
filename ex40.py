class  Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def sos(self, x):
        print(f"do some {x}")

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pocket full of shells"])

learn_python = Song(["Now time is come, now or newer",
                     "To learn the Python",
                     "To make it happens!"])

lir = ["We all be doomed soon!",
        "And very soon!"]




song = Song(lir)
song.sing_me_a_song()
song.sos("All goes according to plan!")

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

learn_python.sing_me_a_song()
