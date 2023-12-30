import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tetris Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define game variables
block_size = 30
grid_width = window_width // block_size
grid_height = window_height // block_size
grid = [[BLACK] * grid_width for _ in range(grid_height)]

# Define Tetromino shapes
tetrominoes = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

# Define Tetromino colors
tetromino_colors = [RED, GREEN, BLUE]

# Define game functions
def draw_grid():
    for row in range(grid_height):
        for col in range(grid_width):
            pygame.draw.rect(window, grid[row][col], (col * block_size, row * block_size, block_size, block_size))

def draw_tetromino(tetromino, x, y, color):
    for row in range(len(tetromino)):
        for col in range(len(tetromino[row])):
            if tetromino[row][col]:
                pygame.draw.rect(window, color, ((x + col) * block_size, (y + row) * block_size, block_size, block_size))

def generate_new_tetromino():
    tetromino = random.choice(tetrominoes)
    color = random.choice(tetromino_colors)
    x = (grid_width - len(tetromino[0])) // 2
    y = 0
    return tetromino, x, y, color

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(10)  # Limit the frame rate to 10 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic goes here

    # Drawing code goes here
    window.fill(WHITE)
    draw_grid()
    tetromino, x, y, color = generate_new_tetromino()
    draw_tetromino(tetromino, x, y, color)
    pygame.display.update()

# Quit the game
pygame.quit()
