import pygame

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("برنامه نقاشی - نسخه نرم")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

brush_color = BLACK  

screen.fill(WHITE)


drawing = False
last_pos = None

clock = pygame.time.Clock()

def draw_smooth_line(surface, color, start, end, width):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + dx * i / distance)
        y = int(start[1] + dy * i / distance)
        pygame.draw.circle(surface, color, (x, y), width // 2)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen.fill(WHITE)
            elif event.key == pygame.K_1:
                brush_color = BLACK
            elif event.key == pygame.K_2:
                brush_color = RED
            elif event.key == pygame.K_3:
                brush_color = BLUE

    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        if last_pos:
            draw_smooth_line(screen, brush_color, last_pos, mouse_pos, 6)
        last_pos = mouse_pos
    else:
        last_pos = None

    pygame.display.update()
    clock.tick(60)

pygame.quit()
