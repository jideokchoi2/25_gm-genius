import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid It")

# Colors
WHITE = (255, 255, 255)
RED = (220, 20, 60)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Game settings
FPS = 60
clock = pygame.time.Clock()

# Player settings
PLAYER_SIZE = 50
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - PLAYER_SIZE - 10, PLAYER_SIZE, PLAYER_SIZE)
player_speed = 6

# Enemy settings
ENEMY_SIZE = 40
enemy_speed = 5
enemies = []

# Lives
lives = 3

# Font
font = pygame.font.SysFont(None, 36)

# Enemy spawn timer
SPAWN_INTERVAL = 1000  # milliseconds
enemy_event = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_event, SPAWN_INTERVAL)

def spawn_enemies():
    for _ in range(2):
        x = random.randint(0, WIDTH - ENEMY_SIZE)
        enemy = pygame.Rect(x, -ENEMY_SIZE, ENEMY_SIZE, ENEMY_SIZE)
        enemies.append(enemy)

def move_enemies():
    for enemy in enemies:
        enemy.y += enemy_speed
    # Remove enemies that are off-screen
    enemies[:] = [e for e in enemies if e.y < HEIGHT + ENEMY_SIZE]

def check_collisions():
    global lives
    for enemy in enemies[:]:
        if player.colliderect(enemy):
            enemies.remove(enemy)
            lives -= 1
            if lives <= 0:
                return True  # Game over
    return False

def draw_window():
    WINDOW.fill(WHITE)

    # Draw player
    pygame.draw.rect(WINDOW, GREEN, player)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(WINDOW, RED, enemy)

    # Draw lives
    lives_text = font.render(f"Lives: {lives}", True, BLACK)
    WINDOW.blit(lives_text, (10, 10))

    pygame.display.update()

def main():
    global lives
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == enemy_event:
                spawn_enemies()

        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x < WIDTH - PLAYER_SIZE:
            player.x += player_speed
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= player_speed
        if keys[pygame.K_DOWN] and player.y < HEIGHT - PLAYER_SIZE:
            player.y += player_speed

        move_enemies()
        is_game_over = check_collisions()

        if is_game_over:
            print("💀 Game Over! You lost all your lives.")
            pygame.time.wait(1500)
            running = False

        draw_window()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
