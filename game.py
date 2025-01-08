import pygame
import random
import sys

# 초기화
pygame.init()

# 화면 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Birds")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# FPS 설정
clock = pygame.time.Clock()
FPS = 60

# 플레이어 설정
player_width = 50
player_height = 20
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 10

# 새 설정
bird_width = 40
bird_height = 40
bird_x = random.randint(0, SCREEN_WIDTH - bird_width)
bird_y = -bird_height
bird_speed = 5

# 점수
score = 0
font = pygame.font.Font(None, 36)

def draw_player(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, player_width, player_height))

def draw_bird(x, y):
    pygame.draw.ellipse(screen, RED, (x, y, bird_width, bird_height))

def show_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# 게임 루프
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    # 새 이동
    bird_y += bird_speed

    # 충돌 감지
    if (player_x < bird_x < player_x + player_width or player_x < bird_x + bird_width < player_x + player_width) and bird_y + bird_height > player_y:
        score += 1
        bird_x = random.randint(0, SCREEN_WIDTH - bird_width)
        bird_y = -bird_height

    # 새가 화면을 벗어났을 때
    if bird_y > SCREEN_HEIGHT:
        bird_x = random.randint(0, SCREEN_WIDTH - bird_width)
        bird_y = -bird_height

    # 객체 그리기
    draw_player(player_x, player_y)
    draw_bird(bird_x, bird_y)
    show_score()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
