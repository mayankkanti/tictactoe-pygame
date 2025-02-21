import pygame

def pvb(screen, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "game_select"
        
        screen.fill((0, 0, 0))
        font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 50)
        title_text = font.render("PvB", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(300, 100))
        screen.blit(title_text, title_rect)
        
        font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 35)
        title_text = font.render("Player Vs Bot", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(300, 150))
        screen.blit(title_text, title_rect)
        
        font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 20)
        subtitle_text = font.render("Coming Soon...!", True, (255, 255, 255))
        subtitle_rect = subtitle_text.get_rect(center=(300, 300))
        screen.blit(subtitle_text, subtitle_rect)
        
        font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 18)
        back_text = font.render("Press ESC to go back", True, (255, 255, 255))
        back_rect = back_text.get_rect(center=(300, 500))
        screen.blit(back_text, back_rect)
        
        
        pygame.display.update()
        clock.tick(60)