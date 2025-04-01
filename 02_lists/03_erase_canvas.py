import pygame

import time
pygame.init()
    
CANVAS_WIDTH : int = 400
CANVAS_HEIGHT : int = 400

CELL_SIZE : int = 40
ERASER_SIZE : int = 20

BLUE = (0,0,225)
WHITE = (225,225,225)
PINK = (125,126,234)

screen = pygame.display.set_mode((CANVAS_WIDTH,CANVAS_HEIGHT))
pygame.display.set_caption("Enter effect in pygame")

grid = []
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        rect = pygame.Rect(col, row , CELL_SIZE,CELL_SIZE)
        grid.append(rect)

eraser = pygame.Rect(200,200,ERASER_SIZE,ERASER_SIZE)

running = True
while running:
    screen.fill(WHITE)

    for rect in grid:
        pygame.draw.rect(screen,BLUE,rect)

    mouse_x , mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x,mouse_y)

    new_grid = []
    for rect in grid:
        if not eraser.colliderect(rect):
            new_grid.append(rect)
    grid = new_grid

    pygame.draw.rect(screen, PINK, eraser)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    time.sleep(0.05)
pygame.quit()