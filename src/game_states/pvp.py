import pygame
import numpy as np
from .end_screen import end

def draw_board(screen):
    board_img = pygame.image.load("../tictactoe-pygame/src/assets/images/board.png")
    board_img = pygame.transform.scale(board_img, (450, 450))
    board_rect = board_img.get_rect(center=(300, 300))
    screen.blit(board_img, board_rect)

def draw_moves(screen, board, cell_boundaries):
    for row in range(3):
        for col in range(3):
            if board[row][col] is not None:
                center_x = (cell_boundaries[row][col][0] + cell_boundaries[row][col][2])// 2
                center_y = (cell_boundaries[row][col][1] + cell_boundaries[row][col][3])// 2
                if board[row][col] == "X":
                    x_img = pygame.image.load("../tictactoe-pygame/src/assets/images/cross.png")
                    x_img = pygame.transform.scale(x_img, (100, 100))
                    x_rect = x_img.get_rect(center=(center_x, center_y))
                    screen.blit(x_img, x_rect)
                elif board[row][col] == "O":
                    o_img = pygame.image.load("../tictactoe-pygame/src/assets/images/circle.png")
                    o_img = pygame.transform.scale(o_img, (100, 100))
                    o_rect = o_img.get_rect(center=(center_x, center_y))
                    screen.blit(o_img, o_rect)



def animate_win_diagonal(screen, board, cell_boundaries, row1, col1, row2, col2):
    pygame.draw.line(screen, (0, 255, 0), (cell_boundaries[row1][col1][0] + 25, cell_boundaries[row1][col1][1] + 25),(cell_boundaries[row2][col2][2] - 25, cell_boundaries[row2][col2][3] - 25), 5)
    pygame.display.flip()
    pygame.time.delay(1000)

def check_winner(screen, board, cell_boundaries):
    # returns the winner else None
    # checks rows 
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            animate_win_diagonal(screen, board, cell_boundaries, row, 0, row, 2)
            return board[row][0]
    # checks columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            animate_win_diagonal(screen, board, cell_boundaries, 0, col, 2, col)
            return board[0][col]
    # checks diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        animate_win_diagonal(screen, board, cell_boundaries, 0, 0, 2, 2)
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        animate_win_diagonal(screen, board, cell_boundaries, 0, 2, 2, 0)
        return board[0][2]
    # checks for draw
    if np.all(board != None):
        return "draw"
    return None

def pvp(screen, clock):
    cell_boundaries = [
    [(75, 125, 181, 234), (186, 114, 378, 211), (387, 100, 525, 197)],
    [(64, 263, 191, 392), (194, 244, 388, 370), (395, 211, 535, 353)],
    [(64, 424, 191, 520), (200, 405, 406, 518), (406, 372, 543, 510)]
    ]
    
    turn = 0 # even turns are player1 and odd turns are player2
    board = np.full((3, 3), None)
    select = pygame.mixer.Sound("../tictactoe-pygame/src/assets/sounds/select1.wav")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "game_select"
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]  # x
                mouseY = event.pos[1]  # y
                if event.button == 1:
                    clicked_row, clicked_col = None, None
                    for row in range(3):
                        for col in range(3):
                            if cell_boundaries[row][col][0] <= mouseX <= cell_boundaries[row][col][2] and \
                            cell_boundaries[row][col][1] <= mouseY <= cell_boundaries[row][col][3]:
                                clicked_row, clicked_col = row, col
                    if clicked_row is not None and clicked_col is not None:
                        if board[clicked_row][clicked_col] is None:
                            if turn % 2 == 0:
                                board[clicked_row][clicked_col] = "X"
                            else:
                                board[clicked_row][clicked_col] = "O"
                            turn += 1
                            select.play() 
        screen.fill((0, 0, 0))
        if turn % 2 == 0:
            font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 20)
            title_text = font.render("Player 1's turn", True, (255, 255, 255))
            title_rect = title_text.get_rect(center=(300, 50))
            screen.blit(title_text, title_rect)
        else:
            font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 20)
            title_text = font.render("Player 2's turn", True, (255, 255, 255))
            title_rect = title_text.get_rect(center=(300, 50))
            screen.blit(title_text, title_rect)
        draw_board(screen)
        draw_moves(screen, board, cell_boundaries)
        if check_winner(screen, board, cell_boundaries) is not None:
            game_state = end(screen, clock, check_winner(screen, board, cell_boundaries))
            return game_state
            
        pygame.display.flip()    
        pygame.display.update()
        clock.tick(60)