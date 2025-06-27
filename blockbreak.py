import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 설정
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("벽돌깨기 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 패들 설정
paddle_width = 100
paddle_height = 10
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - 40
paddle_speed = 5

# 공 설정
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 4  # x축 속도
ball_dy = -4  # y축 속도

# 벽돌 설정
brick_width = 80
brick_height = 30
brick_rows = 5
brick_cols = WIDTH // brick_width
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        bricks.append(pygame.Rect(col * brick_width, row * brick_height + 50, brick_width - 2, brick_height - 2))

# 게임 변수
score = 0
clock = pygame.time.Clock()
running = True

# 게임 루프
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 이동 (마우스)
    paddle_x = pygame.mouse.get_pos()[0] - paddle_width // 2
    paddle_x = max(0, min(paddle_x, WIDTH - paddle_width))  # 경계 제한

    # 공 이동
    ball_x += ball_dx
    ball_y += ball_dy

    # 공 경계 충돌
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_dx = -ball_dx
    if ball_y - ball_radius < 0:
        ball_dy = -ball_dy
    if ball_y + ball_radius > HEIGHT:
        running = False  # 공 아래로 떨어지면 게임 오버

    # 패들과 공 충돌
    paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    if paddle.collidepoint(ball_x, ball_y) and ball_dy > 0:
        ball_dy = -ball_dy

    # 벽돌 충돌
    for brick in bricks[:]:
        if brick.collidepoint(ball_x, ball_y):
            ball_dy = -ball_dy
            bricks.remove(brick)
            score += 10

    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), ball_radius)
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)
    pygame.display.flip()

    # 점수 표시
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"점수: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # FPS 설정
    clock.tick(60)

# 게임 종료
pygame.quit()
print(f"게임 오버! 최종 점수: {score}")