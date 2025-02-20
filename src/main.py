# tic tac toe game with pygame

import pygame
from utils import clock
from game_states.main_menu import main_menu

pygame.init()

height = 600
width = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

game_state = "main_menu"


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if game_state == "main_menu":
        game_state = main_menu(screen, clock)
        print("Leaving main menu")