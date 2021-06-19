import pygame
pygame.init()

# frames per second
FPS = 60

# colours
WHITE = (255, 255, 255)

# block dimensions
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 50
BLOCK_MARGIN = 10

grid = [[0 for x in range(10)] for y in range(10)]

sample = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

# create game screen
SCREEN_SIZE = (700, 700)
screen = pygame.display.set_mode(SCREEN_SIZE)

# manage update speed
clock = pygame.time.Clock()

# game loop
quitting = False
while not quitting:
    # exit when user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitting = True

    for row in range(1, 10):
        for col in range(1, 10):
            pygame.draw.rect(screen, WHITE, ((BLOCK_MARGIN+BLOCK_WIDTH)*row, (BLOCK_MARGIN+BLOCK_WIDTH)*col, BLOCK_WIDTH, BLOCK_HEIGHT))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()