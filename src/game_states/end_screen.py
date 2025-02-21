import pygame
def end(screen, clock, result):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "main_menu"
        screen.fill((0, 0, 0))
        if result == 'draw':
            font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 20)
            title_text = font.render("It's a draw!", True, (255, 255, 255))
            title_rect = title_text.get_rect(center=(300, 50))
            screen.blit(title_text, title_rect)
        else:
            if result == 'X':
                font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 20)
                title_text = font.render("Player 1 wins!", True, (255, 255, 255))
                title_rect = title_text.get_rect(center=(300, 50))
                screen.blit(title_text, title_rect)
            else:
                font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 20)
                title_text = font.render("Player 2 wins!", True, (255, 255, 255))
                title_rect = title_text.get_rect(center=(300, 50))
                screen.blit(title_text, title_rect)
        font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 20)
        title_text = font.render("Press 'ESC' to go back!", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(300, 100))
        screen.blit(title_text, title_rect)
        pygame.display.update()
        clock.tick(60)