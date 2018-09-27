from random import randint

class Die():
    """ Die class """

    def __init__(self, num_sides=6):
        """ default die is 6 """
        self.num_sides = num_sides

    def roll(self):
        """ return a value of 1 to sides number """
        return randint(1, self.num_sides)
