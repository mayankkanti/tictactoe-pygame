# tic tac toe game with pygame

import pygame
from utils import clock
from game_states.main_menu import main_menu
from game_states.game_select import game_select
from game_states.pvp import pvp
from game_states.pvb import pvb

pygame.init()
pygame.mixer.init()

height = 600
width = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

game_state = "main_menu"
bgm = pygame.mixer.Sound("../tictactoe-pygame/src/assets/sounds/bgm.mp3")
bgm.play(loops=-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if game_state == "main_menu":
        game_state = main_menu(screen, clock)
    if game_state == "game_select":
        game_state = game_select(screen, clock)
    if game_state == "PvP":
        game_state = pvp(screen, clock)
    if game_state ==  "PvB":
        game_state = pvb(screen, clock)