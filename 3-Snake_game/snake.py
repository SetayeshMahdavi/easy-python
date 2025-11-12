import pygame
import random

RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (152, 255, 152)  
BLUE=(20, 50, 128)  
window = pygame.display.set_mode((800, 800))

snake = [[0, 0], [50, 0], [100, 0]]
block = 50
x_change = 50
y_change = 0
step = 50

head_img = pygame.image.load("head.png")
head_img = pygame.transform.scale(head_img, (block,block))
food_img=pygame.image.load("food.png")
food_img=pygame.transform.scale(food_img,(70,70))

def random_food():
    x_food = random.choice(range(0, 750, 50))
    y_food = random.choice(range(0, 750, 50))
    return x_food, y_food

x_food, y_food = random_food()
clock = pygame.time.Clock()

runing = True
while runing:
    clock.tick(10)
    window.fill(BLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y_change = step
                x_change = 0
            if event.key == pygame.K_UP:
                y_change = -step
                x_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = step
                y_change = 0
            if event.key == pygame.K_LEFT:
                x_change = -step
                y_change = 0

    snake.append([snake[-1][0] + x_change, snake[-1][1] + y_change])

    if snake[-1][0] > 800:
        snake[-1][0] = 0
    if snake[-1][0] < 0:
        snake[-1][0] = 800
    if snake[-1][1] > 800:
        snake[-1][1] = 0
    if snake[-1][1] < 0:
        snake[-1][1] = 800

    for i in snake[:-1]:
        if i == snake[-1]:
            runing = False

    if snake[-1] == [x_food, y_food]:
        x_food, y_food = random_food()
    else:
        snake.pop(0)

    for pos in snake[:-1]:
        pygame.draw.rect(window, GREEN, [pos[0], pos[1], block - 4, block - 4])

        
    head_rotated = head_img
    if x_change > 0:
        head_rotated = pygame.transform.rotate(head_img, 270)
    elif x_change < 0:
        head_rotated = pygame.transform.rotate(head_img, 90)
    elif y_change > 0:
        head_rotated = pygame.transform.rotate(head_img, 180)
    elif y_change < 0:
        head_rotated = head_img
    window.blit(head_rotated, (snake[-1][0], snake[-1][1]))

    # pygame.draw.rect(window, RED, [x_food, y_food, block, block])
    window.blit(food_img,[x_food,y_food])

    pygame.display.update()
