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



def check_winner(board):
    # returns the winner else None
    # checks rows 
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]
    # checks columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    # checks diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
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
    print(board)
    
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
                if event.button == 1:
                    print(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]  # x
                mouseY = event.pos[1]  # y

                # Determine clicked cell
                clicked_row, clicked_col = None, None
                for row in range(3):
                    for col in range(3):
                        if cell_boundaries[row][col][0] <= mouseX <= cell_boundaries[row][col][2] and \
                        cell_boundaries[row][col][1] <= mouseY <= cell_boundaries[row][col][3]:
                            clicked_row, clicked_col = row, col
                            print(f"Col: {clicked_col} Row: {clicked_row}")
                if clicked_row is not None and clicked_col is not None:
                    if board[clicked_row][clicked_col] is None:
                        if turn % 2 == 0:
                            board[clicked_row][clicked_col] = "X"
                        else:
                            board[clicked_row][clicked_col] = "O"
                        turn += 1
                        select.play()
                        print(board)
            
        
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
        if check_winner(board) is not None:
            game_state = end(screen, clock, check_winner(board))
            return game_state
            
        pygame.display.flip()    
        pygame.display.update()
        clock.tick(60)