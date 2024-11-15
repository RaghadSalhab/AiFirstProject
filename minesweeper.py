import pygame
import random
import sys
import time

# Initialize Pygame and the mixer for sounds
pygame.init()
pygame.mixer.init()

# Screen settings
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 10  # 10x10 grid
CELL_SIZE = WIDTH // GRID_SIZE
NUM_MINES = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.SysFont(None, 24)
large_font = pygame.font.SysFont(None, 36)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# Load sounds
lose_sound = pygame.mixer.Sound("lose_sound.wav")
win_sound = pygame.mixer.Sound("win_sound.wav")
click_sound = pygame.mixer.Sound("click_sound.wav")

def display_loading_screen():
    screen.fill(BLACK)
    loading_text = large_font.render("Loading...", True, WHITE)
    bar_width = 200
    bar_height = 20
    bar_x = (WIDTH - bar_width) // 2
    bar_y = (HEIGHT - bar_height) // 2 + 40

    for progress in range(0, bar_width + 1, 10):  # Simulated loading progress
        screen.fill(BLACK)
        
        # Display loading text
        screen.blit(loading_text, ((WIDTH - loading_text.get_width()) // 2, (HEIGHT - loading_text.get_height()) // 2 - 30))
        
        # Draw the progress bar background
        pygame.draw.rect(screen, GRAY, (bar_x, bar_y, bar_width, bar_height))
        
        # Draw the progress bar fill
        pygame.draw.rect(screen, GREEN, (bar_x, bar_y, progress, bar_height))
        
        pygame.display.flip()
        pygame.time.delay(100)  # Delay to simulate loading

def initialize_game():
    # Set up global variables for grid, revealed, and flagged states
    global grid, revealed, flagged, mine_positions, game_over
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    flagged = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    game_over = False

    # Place mines
    mine_positions = set()
    while len(mine_positions) < NUM_MINES:
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        mine_positions.add((x, y))
        grid[y][x] = -1  # -1 represents a mine

    # Calculate numbers around mines
    for x, y in mine_positions:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and grid[ny][nx] != -1:
                    grid[ny][nx] += 1

def draw_grid():
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if revealed[y][x]:
                pygame.draw.rect(screen, WHITE, rect)
                if grid[y][x] > 0:
                    text = font.render(str(grid[y][x]), True, BLACK)
                    screen.blit(text, (x * CELL_SIZE + 10, y * CELL_SIZE + 10))
                elif grid[y][x] == -1:
                    pygame.draw.circle(screen, BLACK, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 10)
            else:
                pygame.draw.rect(screen, GRAY, rect)
                if flagged[y][x]:
                    pygame.draw.circle(screen, RED, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 5)
            pygame.draw.rect(screen, BLACK, rect, 1)

def reveal_cell(x, y):
    global game_over
    if not revealed[y][x] and not flagged[y][x]:
        revealed[y][x] = True
        click_sound.play()  # Play click sound on revealing a cell
        if grid[y][x] == -1:
            game_over = True  # Trigger game over if a mine is revealed
            reveal_all_mines()
            lose_sound.play()  # Play lose sound on game over
        elif grid[y][x] == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                        reveal_cell(nx, ny)
        check_win()

def reveal_all_mines():
    for x, y in mine_positions:
        revealed[y][x] = True

def toggle_flag(x, y):
    if not revealed[y][x]:
        flagged[y][x] = not flagged[y][x]

def draw_game_over():
    # Background rectangle for the text
    pygame.draw.rect(screen, GRAY, (WIDTH // 2 - 100, HEIGHT // 2 - 40, 200, 80))
    
    # "Game Over" text
    game_over_text = large_font.render("Game Over!", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 30))
    
    # "Press 'R' to Restart" text
    restart_text = font.render("Press 'R' to Restart", True, BLACK)
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 10))

def check_win():
    # Check if all non-mine cells have been revealed
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if grid[y][x] != -1 and not revealed[y][x]:
                return  # If there's an unrevealed non-mine cell, the player hasn't won yet
    win_sound.play()  # Play win sound if all non-mine cells are revealed
    print("You Win!")
    pygame.time.delay(2000)  # Wait 2 seconds before closing
    pygame.quit()
    sys.exit()

# Main game loop
display_loading_screen()  # Show loading animation at the start
initialize_game()
running = True
while running:
    screen.fill(BLACK)
    draw_grid()
    if game_over:
        draw_game_over()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:  # Press 'R' to restart
                initialize_game()  # Reset the game
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE
            if event.button == 1:  # Left click to reveal
                reveal_cell(x, y)
            elif event.button == 3:  # Right click to flag
                toggle_flag(x, y)

    pygame.display.flip()

pygame.quit()
