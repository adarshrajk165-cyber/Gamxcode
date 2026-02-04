import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gamxcode - Survival Demo")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

# Player
player_size = 40
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Hunger system
hunger = 100

running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    hunger -= 0.02
    if hunger < 0:
        hunger = 0

    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))

    hunger_text = font.render(f"Hunger: {int(hunger)}", True, BLACK)
    screen.blit(hunger_text, (10, 10))

    pygame.display.update()

pygame.quit()
sys.exit()
