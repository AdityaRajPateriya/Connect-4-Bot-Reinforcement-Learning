from Player import Player


class HumanPlayer(Player):
    """A class that represents a human player in the game"""

    def __init__(self, coin_type):
        """
        Initialize a human player with their coin type
        """
        Player.__init__(self, coin_type)
