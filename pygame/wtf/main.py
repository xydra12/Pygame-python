import pygame
import random


pygame.init()


WINDOW_WIDTH = 1266
WINDOW_HEIGHT = 668
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("wtf is this")


GRASS_COLOR = (0, 255, 0)
DIRT_COLOR = (139, 69, 19)
STONE_COLOR = (128, 128, 128)


BLOCK_SIZE = 50


player_x = WINDOW_WIDTH // 2
player_y = WINDOW_HEIGHT // 2
player_speed = 5


running = True
while running:
   
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

   
    game_window.fill((0, 0, 0))

    
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            
            block_type = random.randint(1, 3)
            if block_type == 1:
                block_color = GRASS_COLOR
            elif block_type == 2:
                block_color = DIRT_COLOR
            else:
                block_color = STONE_COLOR

            
            pygame.draw.rect(game_window, block_color, (x, y, BLOCK_SIZE, BLOCK_SIZE))

    
    pygame.draw.rect(game_window, (255, 255, 255), (player_x, player_y, BLOCK_SIZE, BLOCK_SIZE))

    
    pygame.display.flip()


pygame.quit()
