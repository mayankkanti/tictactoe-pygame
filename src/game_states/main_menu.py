import pygame


def main_menu_text(screen, tilted_alpha):
    
    font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 50)
    title_text = font.render("Tic Tac Toe", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(300, 100))
    screen.blit(title_text, title_rect)
    
    tictactoe = pygame.image.load("../tictactoe-pygame/src/assets/images/tictactoe.png")
    tictactoe = pygame.transform.scale(tictactoe, (300, 300))
    tictactoe_rect = tictactoe.get_rect(center=(300, 300))
    screen.blit(tictactoe, tictactoe_rect)  
    
    font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 20)
    enter_text = font.render("Press Enter to start", True, (255, 255, 255))
    enter_text.set_alpha(tilted_alpha)
    enter_rect = enter_text.get_rect(center=(300, 500))
    screen.blit(enter_text, enter_rect)
    pygame.display.flip()

def main_menu(screen, clock):
    tilted_alpha = 255
    alpha_direction = -1
    select = pygame.mixer.Sound("../tictactoe-pygame/src/assets/sounds/select.mp3")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    select.play()
                    return "game_select"
        
        tilted_alpha += alpha_direction * 5
        if tilted_alpha >= 255 or tilted_alpha <= 0:
            alpha_direction *= -1
        
        screen.fill((0, 0, 0))
        main_menu_text(screen, tilted_alpha) 
        
        pygame.display.update()
        clock.tick(60)
