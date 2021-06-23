import pygame
pygame.init()

# create game screen
SCREEN_SIZE = (500, 500)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Sudoku Solver')

pygame.quit()
