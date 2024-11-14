
# 🧩 Minesweeper Game

A simple Minesweeper game built with Python and Pygame. The game features a classic Minesweeper board where players reveal cells to avoid mines and flag suspected mine locations.

## 🎮 Features

- **⏳ Loading Screen Animation**: A simulated progress bar shows at the beginning, giving a loading animation.
- **🕹️ Interactive Minesweeper Gameplay**: Players can reveal cells or flag suspected mines.
- **💥 Game Over Detection**: If a player clicks on a mine, the game reveals all mines and displays a "Game Over" message.
- **🔄 Restart Option**: Press 'R' to restart the game after a game over.

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AiFirstProject/minesweeper.git
   cd minesweeper
   ```

2. **Install Requirements**
   - Make sure Python and Pygame are installed.
   - Install Pygame if necessary:
     ```bash
     pip install pygame
     ```

## 🚀 Running the Game

1. **Start the Game**
   ```bash
   python minesweeper.py
   ```

2. **Gameplay Instructions**
   - **🖱️ Left Click**: Reveal a cell.
   - **🔴 Right Click**: Flag or unflag a cell.
   - **🔁 Press "R"**: Restart the game after a game over.

3. **Objective**
   - Reveal all cells without mines to win the game.
   - If you reveal a mine, the game ends with a "Game Over" message.

## 🛠️ Code Overview

- `display_loading_screen()`: Displays a loading animation at the beginning of the game.
- `initialize_game()`: Sets up the Minesweeper grid with random mines and numbers for each cell.
- `draw_grid()`: Draws the Minesweeper grid and updates it based on revealed and flagged cells.
- `reveal_cell(x, y)`: Reveals a cell, and if it's a mine, triggers a game over.
- `toggle_flag(x, y)`: Flags or unflags a cell when the right mouse button is clicked.
- `draw_game_over()`: Displays the "Game Over" message and instructions to restart the game.

## 📸 Screenshots

> **Add screenshots of the game here if possible to show gameplay and game-over screens.**

## ⚙️ Requirements

- Python 3.x
- Pygame library (`pip install pygame`)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy playing Minesweeper! 🎉💣🚩


