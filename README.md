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
- use the following command to clone the repository
  - `git clone https://github.com/YourUsername/Connect4-Reinforcement-Learning-Bot.git`
- Download The Requirments
    - `pip install pygame`
- To run the project simply execute the below command in your terminal
    - `python GameRunner.py`
- you can choose from 2 options play with AI and Train
- click on Train it will play 50 matches with itself we can change the number of iterations by passing it during runtime 
- Use the right and left arrow keys two Move the Coin and press enter to insert the coin/

- Use Train Agent Option before playing with it 
To train the agent, select Train Computer in the main menu. It will play iterations games which was passed as an argument to the program.After training the computer, when 'vs Computer' option is selected, a human can play against the trained computer.Each time 'Train Computer' mode is selected, it trains from the beginning. The state space is all the states which each player sees. For the first player it consists all the boards with an even number of disks, while for the second player it is all the boards with an odd number of disks.The action space will be the numbers 1–7 for each column a player can play.The reward will be 1 for winning, -1 for losing, 0.5 for a tie and 0 otherwise. Note here that like in every 2-players’ game, the next state is not determined by the action taken because it depends also on the opponent’s action. The transition probability between 2 states depends on both the player’s and the opponent’s policies.

