from typing import Dict
import pygame
pygame.init()

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

# colours
WHITE = (255, 255, 255)
LIGHT_BROWN = (224, 190, 151)
LIGHT_BLUE = (200, 255, 255)
BLACK = (0, 0, 0)
GREY = (89, 89, 89)

# fonts
font = pygame.font.SysFont(None, 32)

# create game screen
SCREEN_SIZE = (541, 541)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Sudoku Solver')

# current block
curr_x = 0
curr_y = 0

# to divide screen into 9x9 grid
DIV = 540/9

def get_block(pos):
    global curr_x
    curr_x = pos[0]//DIV

    global curr_y
    curr_y = pos[1]//DIV

    return (curr_x, curr_y)

def draw_lines():
    # Draw lines to form grid          
    for i in range(10):
        if i % 3 == 0 :
            thickness = 3
        else:
            thickness = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * DIV), (540, i * DIV), thickness)
        pygame.draw.line(screen, (0, 0, 0), (i * DIV, 0), (i * DIV, 540), thickness)   

def display_sudoku(sudoku):
    for i in range (9):
        for j in range (9):
            if sudoku[i][j]!= 0:
 
                # Fill grey color in default numbered blocks
                pygame.draw.rect(screen, GREY, (i * DIV, j * DIV, DIV+1, DIV+1))
 
                # Fill default numbers
                text1 = font.render(str(sudoku[i][j]), 1, LIGHT_BROWN)
                screen.blit(text1, (i * DIV + 25, j * DIV + 22))

# game loop
quitting = False
while not quitting:

    screen.fill(LIGHT_BROWN)
    display_sudoku(sample)
    draw_lines()

    for event in pygame.event.get():
        
        # exit when user quits  
        if event.type == pygame.QUIT:
            quitting = True
        
        # find where the mouse is
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(get_block(pygame.mouse.get_pos()))

    pygame.display.update()

pygame.quit()
