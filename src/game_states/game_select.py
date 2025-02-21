import pygame


def menu_text(screen,font1, font2, tilted_alpha1, tilted_alpha2):
    
    font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 50)
    title_text = font.render("Tic Tac Toe", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(300, 100))
    screen.blit(title_text, title_rect)
    
    font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", font1)
    player_text = font.render("Player Vs. Player", True, (255, 255, 255))
    player_rect = player_text.get_rect(center=(300, 250))
    screen.blit(player_text, player_rect)
    if font1 == 30: pygame.draw.line(screen, (255, 255, 255), (150, 280), (450, 280), 2)
    
    font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", font2)
    player_text = font.render("Player Vs. Bot", True, (255, 255, 255))
    player_rect = player_text.get_rect(center=(300, 350))
    screen.blit(player_text, player_rect)
    if font2 == 30: pygame.draw.line(screen, (255, 255, 255), (150, 400), (450, 400), 2)
    
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
    
    font = pygame.font.Font("../tictactoe-pygame/src/assets/fonts/PressStart2P.ttf", 18)
    back_text = font.render("Press ESC to go back", True, (255, 255, 255))
    back_rect = back_text.get_rect(center=(300, 550))
    screen.blit(back_text, back_rect)
    
    pygame.display.flip()

def game_select(screen, clock):
    tilted_alpha1 = 255
    alpha_direction1 = -1
    tilted_alpha2 = 255
    alpha_direction2 = -1
    options = ["PvP", "PvB"]
    selected_option = 0
    
    select = pygame.mixer.Sound("../tictactoe-pygame/src/assets/sounds/select.mp3")
    
    font1 = 25
    font2 = 25
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(f"Selected option: {options[selected_option]}")
                    select.play()
                    return options[selected_option]
                if event.key == pygame.K_UP:
                    selected_option -= 1
                    if selected_option < 0:
                        selected_option = 0
                if event.key == pygame.K_DOWN:
                    selected_option += 1
                    if selected_option >= len(options):
                        selected_option = len(options) - 1
                if event.key == pygame.K_ESCAPE:
                    return "main_menu"        
        if selected_option == 0:
            font1 = 30
            font2 = 25
        if selected_option == 1:
            font1 = 25
            font2 = 30
        screen.fill((0, 0, 0))
        menu_text(screen, font1, font2, tilted_alpha1, tilted_alpha2) 
        pygame.display.update()
        clock.tick(60)
