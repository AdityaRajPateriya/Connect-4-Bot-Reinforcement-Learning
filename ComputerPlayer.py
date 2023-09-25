from Player import Player
from QLearningPlayer import QLearningPlayer
from RandomPlayer import RandomPlayer


class ComputerPlayer(Player):
    """A class that represents an AI player in the game"""

    def __init__(self, coin_type, player_type):
        """
        Initialize an AI with the proper type which are one of Random and
        Q-learner currently
        """
        if (player_type == "random"):
            self.player = RandomPlayer(coin_type)
        else:
            self.player = QLearningPlayer(coin_type)

    def complete_move(self, coin, board, game_logic, background):
        """
        Move the coin and decide which slot to drop it in and learn from the
        chosen move
        """
        actions = board.get_available_actions()
        state = board.get_state()
        chosen_action = self.choose_action(state, actions)
        coin.move_right(background, chosen_action)
        coin.set_column(chosen_action)
        game_over = board.insert_coin(coin, background, game_logic)
        self.player.learn(board, actions, chosen_action, game_over, game_logic)

        return game_over

    def get_coin_type(self):
        """
        Return the coin type of the AI player
        """
        return self.player.get_coin_type()

    def choose_action(self, state, actions):
        """
        Choose an action (which slot to drop in) based on the state of the
        board
        """
        return self.player.choose_action(state, actions)
