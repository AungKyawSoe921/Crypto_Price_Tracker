import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple 2D Game")

# Character setup
player_size = 50
player_pos = [screen_width // 2, screen_height // 2]
player_speed = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Ensure the player stays within screen bounds
    if player_pos[0] < 0:
        player_pos[0] = 0
    if player_pos[0] > screen_width - player_size:
        player_pos[0] = screen_width - player_size
    if player_pos[1] < 0:
        player_pos[1] = 0
    if player_pos[1] > screen_height - player_size:
        player_pos[1] = screen_height - player_size

    # Fill the screen with white
    screen.fill(white)

    # Draw the player (a rectangle)
    pygame.draw.rect(screen, black, (player_pos[0], player_pos[1], player_size, player_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)
