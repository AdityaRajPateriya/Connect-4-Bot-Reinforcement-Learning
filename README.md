# Connect Four Game

This Project is an implementation of the classic Connect Four game using Python and pygame. It includes AI players which can play against humans

## AI Bot Strategy

Our AI bot in this Connect Four game utilizes Q-learning, a reinforcement learning technique, to make intelligent moves. Q-learning allows the bot to learn from its past experiences and adapt its strategy over time.
There are other algorithms also such minimax which is a Tree seach based algo and caa take time to respond as it need to search the decision tree\

There are Other Deep learning Techniques (DQN and models such as AlphaGoZero) which really give good results but we will go with Qlearing as it si simpler to understand and implemet and also gives good result

### Q-Learning Overview

Q-learning is a machine learning algorithm that helps the AI bot make decisions based on the expected rewards of different actions. In the context of Connect Four, our AI bot learns to:

- Evaluate the current state of the game board.
- Predict the value of taking various actions (choosing different columns to drop discs).
- Make decisions that maximize its chances of winning or preventing the opponent from winning.


## Folder Structure

The project is organized into several files and folders as follows:
- `Player.py`: Defines the player object.
- `Player2.py`: Represent Human 
- `AIPlayer.py`: Contains the code for the AI player.
- `Board.py`: Implements the game board and its logic.
- `CheckForWin.py`: Handles the logic for checking winning conditions.
- `Coin.py`: Defines the coin object used in the game.
- `GameRunner.py`: Manages the game loop and user interface.
- `QLearningPlayer.py`: Contains updates for the Q-learning AI player.
- `RandomChoice.py`: Contains updates related to random choices.
- `Slot.py`: Defines the slot object.
- `SlotTrackerNode.py`: Contains updates related to slot tracking.
- `isFull.py`: Handles the logic for checking if a slot is full.

## Usage
- use Following comman to cloan the reposatory
  - `git clone https://github.com/YourUsername/Connect4-Reinforcement-Learning-Bot.git`
- Downlaod The Requirments
    - `pip install pygame`
- To run project simply exacute the below comman in you termina
    - `python GameRunner.py
`