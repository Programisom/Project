import pygame
pygame.init()
CUBE_SIZE=25
CUBES_NUM = 20
WIDTH = CUBES_NUM * CUBE_SIZE
screen = pygame.display.set_mode((WIDTH, WIDTH))
BLUE = (41,94,179)
screen.fill(BLUE)
WHITE = (255,255,255)
GREEN = (0,255,0)
pygame.display.update()
def draw_snake_part(x, y):
    position = (x * CUBE_SIZE,
                y * CUBE_SIZE,
                CUBE_SIZE,
                CUBE_SIZE)
    pygame.draw.rect(screen,GREEN,position)
    pygame.display.update()
draw_snake_part(0, 0)
draw_snake_part(13, 16)
draw_snake_part(10, 10)
draw_snake_part(12, 8)
draw_snake_part(19, 19)
def draw_food(x, y):
    radius = float(CUBE_SIZE) /2
    position = (x * CUBE_SIZE + radius,
                y* CUBE_SIZE + radius)
    pygame.draw.circle(screen, WHITE, position, radius)
    pygame.display.update()
draw_food(0,0)
draw_food(13, 16)
draw_food(10,10)
draw_food(12, 8)
draw_food(19, 19)
from position import Position
snake = [
    Position(2,2),
    Position(3,2),
    Position(4,2),
    Position(5,2),
    Position(5, 1)
]
def draw_snake(snake):
    for part in snake:
        draw_snake_part(part.x, part.y)
Food = Position(11, 14)
def draw_snake_part(pos):
    position = (pos.x * CUBE_SIZE,
                pos.y * CUBE_SIZE,
                CUBE_SIZE,
                CUBE_SIZE)
    pygame.draw.rect(screen,GREEN,position)
    pygame.display.update()
def draw_food(pos):
    radius = float(CUBE_SIZE) /2
    position = (pos.x * CUBE_SIZE + radius,
                pos.y * CUBE_SIZE + radius)
    pygame.draw.circle(screen,WHITE,position,radius)
    pygame.display.update()
def draw_snake(snake):
    for part in snake:
        draw_snake_part(part)
screen.fill(BLUE)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
