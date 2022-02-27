# -*- coding: utf-8 -*-
from random import randint
from PyQt5.QtWidgets import QApplication
import numpy as np

class beautycontest:
    """ Constructor.
    """
    def __init__(self):
        self.nb_players = 4
        player1 = player()
        player2 = player()
        player3 = player()
        player4 = player()
        self.players = np.array([player1, player2, player3, player4])
        self.nb_rounds = 2
        self.current_round = 0
        self.p = 1

    """ Calculate the mean of all selected values.
    """
    def mean(self):
        total_value = 0
        nb_values = 0
        i=0
        for player in self.players:
            total_value += player.selected_value
            nb_values += 1
        return total_value/nb_values
    

class player:
    """ Constructor.
    """
    def __init__(self):
        self.name = self.randomname()
        self.score = 0
        self.selected_value = -1

    """ Change the name of the current player.
    """
    def changename(self, newname):
        self.name = newname

    """ Create (by default) a random name for the current player.
    """
    def randomname(self):
        random_string = ""
        for _ in range(10):
            random_integer = randint(97, 97 + 26 - 1)
            flip_bit = randint(0, 1)
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            random_string += (chr(random_integer))
        return random_string

if __name__ == "__main__":
    
    print("\nThis is not the main program !!\n")
   
        
    
        
        
        