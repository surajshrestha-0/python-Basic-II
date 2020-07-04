"""
Imagine you are creating a Super Mario game. You need to define a class to represent Mario.
What would it look like? If you aren't familiar with SuperMario,
use your own favorite video or board game to model a player.
"""


class SuperMario:
    def __init__(self, name, score, coins, level, time, lives):
        self.name = name
        self.score = score
        self.coins = coins
        self.level = level
        self.time = time
        self.lives = lives

    def movement(self):
        # character movement jump (up, down) or walk(left, right)
        pass

    def coins(self):
        # increase number of coins after character collects coins
        pass

    def score(self):
        # increase score after killing enemies or successfully completing different levels
        pass

    def level(self):
        # increase level after successfully completing each level
        pass

    def time(self):
        # keep track of time from the beginning to end of the game
        pass

    def lives(self):
        # decrease lives if character after failing to complete level
        pass

    def end(self):
        # end game after all lives are loss
        pass

