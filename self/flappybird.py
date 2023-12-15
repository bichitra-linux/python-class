import pygame

# Initialize pygame
pygame.init()

# Set up the game window
window_width = 500
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Flappy Bird")

# Game variables
gravity = 0.25
bird_movement = 0
bird_rect = pygame.Rect(100, 100, 50, 50)  # New bird rectangle


# Load game assets (images, sounds, etc.)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     # Update game logic
    bird_movement += gravity
    bird_rect.y += bird_movement

    # Render game objects
    window.fill((255, 255, 255))  # Fill the window with white
    pygame.draw.rect(window, (255, 0, 0), bird_rect)  # Draw the bird
    # Update display
    pygame.display.update()

# Clean up
pygame.quit()
