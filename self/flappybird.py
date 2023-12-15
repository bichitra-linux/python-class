import pygame
import random

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
bird_jump = -12
bird_rect = pygame.Rect(100, 100, 50, 50)
ground_rect = pygame.Rect(0, window_height - 100, window_width, 100)
pipe_width = 100
pipe_height = random.randint(100, 400)
pipe_gap = 200
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)  # New timer event to spawn a new pipe every 1.2 seconds
score = 0  # New variable for the score

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = bird_jump
        if event.type == SPAWNPIPE:  # New event for spawning pipes
            pipe_height = random.randint(100, 400)
            bottom_pipe = pygame.Rect(window_width, window_height - pipe_height, pipe_width, pipe_height)
            top_pipe = pygame.Rect(window_width, 0, pipe_width, window_height - pipe_height - pipe_gap)
            pipe_list.extend((bottom_pipe, top_pipe))

    # Update game logic
    bird_movement += gravity
    bird_rect.y += bird_movement
    pipe_list = [pipe.move(-5, 0) for pipe in pipe_list]  # Move the pipes to the left

    # Collision detection
    for pipe in pipe_list:
        if bird_rect.colliderect(pipe):
            running = False
    if bird_rect.colliderect(ground_rect):
        running = False

    # Scoring
    if len(pipe_list) > 0 and bird_rect.right > pipe_list[0].right and bird_rect.left < pipe_list[0].right + 5:
        score += 1
        pipe_list.pop(0)
        pipe_list.pop(0)

    # Render game objects
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 0, 0), bird_rect)
    pygame.draw.rect(window, (0, 255, 0), ground_rect)
    for pipe in pipe_list:  # Draw all the pipes
        pygame.draw.rect(window, (0, 255, 0), pipe)

    # Draw the score
    score_surface = pygame.font.Font(None, 36).render(str(score), True, (0, 0, 0))
    window.blit(score_surface, (window_width / 2, 100))

    # Update display
    pygame.display.update()

pygame.quit()