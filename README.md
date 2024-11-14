
# 🧩 Minesweeper Game

A simple Minesweeper game built in Python with Pygame. The game lets players reveal cells to avoid mines and flag suspected locations.

## 🎮 Features

- **Loading Animation**: A progress bar at the start.
- **Gameplay**: Reveal cells, flag suspected mines, and avoid clicking on a mine.
- **Game Over and Win Detection**: Sounds play for wins and losses.
- **Restart Option**: Press 'R' to restart after a game over.

## 📦 Set Up and Installation

### Prerequisites

1. **GitHub Account**: [Sign up for GitHub](https://github.com/) if needed.
2. **Tools**:
   - [Download GitHub Desktop](https://desktop.github.com/) for repository management.
   - [Download Visual Studio Code](https://code.visualstudio.com/) for coding and editing.
3. **Python and Pygame**:
   - [Download Python](https://www.python.org/downloads/).
   - Install Pygame after Python is installed:
     ```bash
     pip install pygame
     ```

### Clone Repository

Clone the repository and navigate to the folder:
```bash
git clone https://github.com/AiFirstProject/minesweeper.git
cd minesweeper
```

## 🚀 Running the Game

1. **Start the Game**
   ```bash
   python minesweeper.py
   ```

2. **Controls**
   - **Left Click**: Reveal a cell.
   - **Right Click**: Flag/unflag a cell.
   - **Press "R"**: Restart after a game over.

## 🛠️ Code Overview

- **display_loading_screen**: Shows a loading animation.
- **initialize_game**: Sets up the grid with mines.
- **draw_grid**: Draws the game board.
- **reveal_cell**: Reveals a cell; triggers game over if it's a mine.
- **check_win**: Checks if the player has won by revealing all non-mine cells.

## ⚙️ Requirements

- Python 3.x
- Pygame (`pip install pygame`)

## 📄 License

Licensed under the MIT License.

---

Enjoy Minesweeper! 🎉💣🚩
