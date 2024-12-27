import pygame
import random


pygame.init()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


PLAYER_SIZE = 20
BALL_SIZE = 30
BALL_SPEED = 1


player_x = WINDOW_WIDTH // 2 - PLAYER_SIZE // 2
player_y = WINDOW_HEIGHT - PLAYER_SIZE - 10
player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)


balls = []


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH:
        player_rect.x += 5

    
    if len(balls) < 10 and random.randint(0, 100) < 2:
        ball_x = random.randint(BALL_SIZE, WINDOW_WIDTH - BALL_SIZE)
        ball_y = -BALL_SIZE
        ball_rect = pygame.Rect(ball_x, ball_y, BALL_SIZE, BALL_SIZE)
        balls.append(ball_rect)

    
    for ball in balls:
        ball.y += BALL_SPEED
        if ball.top > WINDOW_HEIGHT:
            balls.remove(ball)

        
        if player_rect.colliderect(ball):
            running = False

    
    game_window.fill(BLACK)

   
    pygame.draw.rect(game_window, WHITE, player_rect)

    
    for ball in balls:
        pygame.draw.rect(game_window, RED, ball)

    
    pygame.display.flip()


pygame.quit()
