import pygame


def menu_text(screen, tilted_alpha1, tilted_alpha2):
    
    font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 50)
    title_text = font.render("Tic Tac Toe", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(300, 100))
    screen.blit(title_text, title_rect)
    
    font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 25)
    player_text = font.render("Player Vs. Player", True, (255, 255, 255))
    player_text.set_alpha(tilted_alpha1)
    player_rect = player_text.get_rect(center=(300, 250))
    screen.blit(player_text, player_rect)
    
    player_text = font.render("Player Vs. Bot", True, (255, 255, 255))
    player_text.set_alpha(tilted_alpha2)
    player_rect = player_text.get_rect(center=(300, 350))
    screen.blit(player_text, player_rect)
    
    font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 15)
    player_text = font.render("(Coming Soon...)", True, (255, 255, 255))
    player_rect = player_text.get_rect(center=(300, 380))
    screen.blit(player_text, player_rect)
    
    up_surface = pygame.image.load("../tictactoe-pygame/src/assets/images/up.png")
    up_surface = pygame.transform.scale(up_surface, (32, 32))
    up_rect = up_surface.get_rect(center=(175, 500))
    screen.blit(up_surface,up_rect)
    
    font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 24)
    up_text = font.render("Up", True, (255, 255, 255))
    up_rect = up_text.get_rect(center=(225, 500))
    screen.blit(up_text, up_rect)
    
    
    down_surface = pygame.image.load("../tictactoe-pygame/src/assets/images/down.png")
    down_surface = pygame.transform.scale(down_surface, (32, 32))
    down_rect = down_surface.get_rect(center=(350, 500))
    screen.blit(down_surface,down_rect)
    
    down_text = font.render("Down", True, (255, 255, 255))
    down_rect = down_text.get_rect(center=(435, 500))
    screen.blit(down_text, down_rect)
    
    pygame.display.flip()

def game_select(screen, clock):
    tilted_alpha1 = 255
    alpha_direction1 = -1
    tilted_alpha2 = 255
    alpha_direction2 = -1
    options = ["PvP", "PvE"]
    selected_option = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(f"Selected option: {options[selected_option]}")
                    return options[selected_option]
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option - 1) % len(options)
        if selected_option == 0:
            tilted_alpha1 += alpha_direction1 * 5
            if tilted_alpha1 >= 255 or tilted_alpha1 <= 0:
                alpha_direction1 *= -1
        else:
            tilted_alpha1 = 255
            
        if selected_option == 1:
            tilted_alpha2 += alpha_direction2 * 5
            if tilted_alpha2 >= 255 or tilted_alpha2 <= 0:
                alpha_direction2 *= -1
        else:
            tilted_alpha2 = 255
            
        
        screen.fill((0, 0, 0))
        menu_text(screen, tilted_alpha1, tilted_alpha2) 
   
        pygame.display.update()
        clock.tick(60)
