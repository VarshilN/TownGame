import pygame
import sys
import MenuButtons.buttons

# Initialize Pygame
pygame.init()

def menu(screen):
    buttons=MenuButtons.buttons
    game_paused=True
    GREY = (169, 169, 169)
    WIDTH,HEIGHT=1920,1080
    con_btn = pygame.image.load('./Images/Buttons/menu_btns/button_continue.png')
    res_btn = pygame.image.load('./Images/Buttons/menu_btns/button_restart-game.png')
    quit_btn = pygame.image.load('./Images/Buttons/menu_btns/button_quit.png')
    background_0 = pygame.image.load('./Images/Background/home_1.png')
    background_0 = pygame.transform.scale(background_0, (WIDTH, HEIGHT))
    con_btn= buttons.Button(650,250,con_btn,0.5)
    res_btn= buttons.Button(650,350,res_btn,0.5)
    quit_btn= buttons.Button(650,450,quit_btn,0.5)
    width = 400
    height=400
    BLACK=(0,0,0)
    while game_paused: 
        # background_screen = pygame.screen(screen.get_size())  # Create a screen with the same size as the screen
        screen.blit(background_0,(0,0))
        # pygame.draw.rect(screen, GREY, (550,150,400,400))
        # pygame.draw.rect(screen, (0, 0, 0), (5,5,5,5), 2)
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0,0,0,150)) 
        screen.blit(overlay, (0, 0))   
        shadow_screen = pygame.Surface((width, height)).convert_alpha()
        shadow_screen.fill((0, 0, 0, 0))
        shadow_rect = pygame.Rect((2, 2), (width, height))
        pygame.draw.rect(shadow_screen, (0, 0, 0, 100), shadow_rect)
        screen.blit(shadow_screen, (550+2,150+2))
        pygame.draw.rect(screen, GREY, (550, 150, width, height))
        pygame.draw.rect(screen, BLACK, (550, 150, width, height), 3)
        #   # Fill the screen with the background color
        con_btn.draw(screen)
        res_btn.draw(screen)
        quit_btn.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if con_btn.draw(screen):
                    game_paused=False
                    return 1
                elif res_btn.draw(screen):
                    game_paused=False
                    return -1
                elif quit_btn.draw(screen):
                    pygame.quit()
        pygame.display.update()
