import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from turtle import Screen, update
import pygame, sys
import time
import exploration_main
from button import Button
from utility import images
I = images()

from exploration_class import SpaceAdventure
import numpy as np

#Initialisation du Pygame
pygame.init()

#Size/Resolution de la window
SCREEN = pygame.display.set_mode((1280,720), pygame.FULLSCREEN)
pygame.display.set_caption("Menu")

#Les images presentes dans le main
#BG = pygame.image.load("Images\BackgroundMenu.png")
#BG = pygame.transform.scale(BG, (1280,720))
#GAMES_BG = pygame.image.load("Images\AmongUsCharacters.png")
#GAMES_BG = pygame.transform.scale(GAMES_BG, (1280,720))
#LEADERBOARD = pygame.transform.scale(pygame.image.load("Images\leaderboard_logo.png"), (40,40))
#LEADERBOARD_H = pygame.transform.scale(pygame.image.load("Images\leaderboard_logo_h.png"), (40,40))
#PROFILE = pygame.transform.scale(pygame.image.load("Images\profile_logo1.png"), (40,40))
#PROFILE_H = pygame.transform.scale(pygame.image.load("Images\profile_logo2.png"), (40,40))



#Font personnalisé
def get_font(size):
    return pygame.font.Font("fonts/font1.ttf", size)

#Liste des jeux
def play(profile_joueur = None):
    if True:
        partie = SpaceAdventure(1)
        start = time.perf_counter()
        end1 = time.perf_counter()
        print(start)
        run = True
        # turn_count = 0
        Loop_count = 0
        while run:
            if (int(end1-start+1) * 10) % 5 == 0:
        #         partie.Galax_On(self.CHECK)
                Loop_count += 1
        #         screen.fill((0,0,0))
                PLAY_MOUSE_POS = pygame.mouse.get_pos()

                partie.displayScreen(SCREEN)

                PLAY_BACK = Button(base_image=None, position=(30, 20), 
                                    text_input="BACK", font=get_font(15), base_color="White", hovering_color="Green")

                PLAY_BACK.changeColor(PLAY_MOUSE_POS)
                PLAY_BACK.update(SCREEN)

                if Loop_count % 35 == 1:
                    partie.avant()
                if len(np.where(partie.tableau == 2)[0]) == 0:
                    run = False
        #         if self.PAUSE:
        #             PAUSE_FOND = pygame.image.load("Images\Large_black_button.png")
        #             PAUSE_FOND_RECT = pygame.image.load("Images\Large_black_button.png").get_rect(center=(640, 300))
        #             PAUSE_TEXT = self.get_font(35).render("Le jeu est en pause, appuyez sur ESC pour continuer", True, "#b68f40")
        #             PAUSE_RECT = PAUSE_TEXT.get_rect(center=(640, 300))
        #             screen.blit(PAUSE_FOND, PAUSE_FOND_RECT)
        #             screen.blit(PAUSE_TEXT, PAUSE_RECT)
                
        #         if partie.mort():
        #             self.PAUSE = True
        #             MORT_FOND = pygame.image.load("Images\Large_black_button.png")
        #             MORT_FOND_RECT = pygame.image.load("Images\Large_black_button.png").get_rect(center=(640, 300))
        #             MORT_TEXT = self.get_font(45).render("Vous êtes mort!", True, "#b68f40")
        #             MORT_RECT = MORT_TEXT.get_rect(center=(640, 300))
        #             SCORE_TEXT = self.get_font(25).render(f'Votre score est : {partie.score_count()}', True, "#b68f40")
        #             SCORE_RECT = SCORE_TEXT.get_rect(center=(640, 335))
        #             screen.blit(MORT_FOND, MORT_FOND_RECT)
        #             screen.blit(MORT_TEXT, MORT_RECT)
        #             screen.blit(SCORE_TEXT, SCORE_RECT)

        #             BACK_DEAD = Button(base_image=pygame.image.load("Images\Black_Button.png"), position=(640, 500), 
        #                                 text_input="OK...", font=self.get_font(35), base_color="#b68f40", hovering_color="Green")

        #             BACK_DEAD.changeColor(PLAY_MOUSE_POS)
        #             BACK_DEAD.update(screen)

        #             DEAD = pygame.image.load("Images\Vert_Mort.png")
        #             DEAD = pygame.transform.scale(DEAD, (55,55))
        #             screen.blit(DEAD, (710, 470))

        #             for event in pygame.event.get():
        #                 if event.type == pygame.QUIT:
        #                     self.money += partie.Money
        #                     pygame.quit()
        #                     sys.exit()
        #                 elif event.type == pygame.MOUSEBUTTONDOWN:
        #                     if event.button == 1:
        #                         if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
        #                             self.money += partie.Money
        #                             self.PAUSE = False
        #                             run = False
        #                             break
        #                         if BACK_DEAD.checkForInput(PLAY_MOUSE_POS):
        #                             self.money += partie.Money + int(partie.score_tot/10)
        #                             self.PAUSE = False
        #                             run = False
        #                             break

        #                 pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                                run = False
                                break
        #             elif event.type == pygame.KEYDOWN and not partie.mort():
        #                 if event.key == pygame.K_ESCAPE:
        #                     self.pause_Switch()
        #                 if not self.PAUSE:
        #                     if event.key == pygame.K_a or event.key == pygame.K_LEFT:
        #                         if self.CHOICE != 5:
        #                             partie.jouer('a')
        #                         self.direction = 'a'
        #                     elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        #                         if self.CHOICE != 5:
        #                             partie.jouer('d')
        #                         self.direction = 'd'
        #                     elif event.key == pygame.K_w or event.key == pygame.K_UP:
        #                         if self.CHOICE != 5:
        #                             partie.jouer('w')
        #                         self.direction = 'w'
        #                     elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        #                         if self.CHOICE != 5:
        #                             partie.jouer('s')
        #                         self.direction = 's'
        #                     if event.key == pygame.K_LSHIFT and self.buy_Stop:
        #                         partie.STOP = True
        #                         if partie.stop_counter == 0:
        #                             partie.stop_counter = 1
        #                     if event.key == pygame.K_SPACE and self.buy_Kame:
        #                         if partie.Kame_counter == 0:
        #                             partie.Kame_counter = 1
        #                             partie.Kamehameha()
        #                     if event.key == pygame.K_a or event.key == pygame.K_LEFT or event.key == pygame.K_d or event.key == pygame.K_RIGHT or event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_s or event.key == pygame.K_DOWN:
        #                         turn_count +=1
        #                         partie.score_count(0)
        #                         if self.CHOICE == 1 and not partie.STOP:
        #                             for _ in range(int(turn_count/20)):
        #                                 partie.spawn ()
        #                             if turn_count % 5 == 0:
        #                                 partie.Boost()
        #                             if not partie.Boost_On:
        #                                 partie.mouv_ennemie()
        #                                 partie.spawn ()
        #                             if partie.Boost_On:
        #                                 partie.Boost_counter()
        #                                 if partie.Boost_count % 2 == 0:
        #                                     partie.mouv_ennemie()
        #                                     partie.spawn ()
        #                         if turn_count%25 == 0:
        #                             partie.dope()
        #                         if (turn_count + 3) % 9 == 0:
        #                             partie.scores(1)
        #                         if (turn_count+2) % 5 == 0:
        #                             partie.scores(2)
        #                         if (turn_count) % 25 == 0:
        #                             partie.scores(3)
        #                         if partie.is_rage():
        #                             partie.Rage_counter()
        #         if not self.PAUSE:
        #             if self.CHOICE == 5:
        #                 if Loop_count % 15 == 0:
        #                     partie.jouer(self.direction)
        #                 if not partie.STOP:
        #                     if Loop_count % 30 == 0:
        #                         for _ in range(int(Loop_count/600)):
        #                             partie.spawn ()
        #                         if Loop_count % 75 == 0:
        #                             partie.Slow_Down()
        #                         if partie.Slow_On:
        #                             partie.Slow_counter()
        #                             if partie.Slow_count % 2 == 0:
        #                                 partie.mouv_ennemie()
        #                                 partie.spawn ()
        #                         if not partie.Slow_On:
        #                             partie.mouv_ennemie()
        #                             partie.spawn ()
        #         if not self.PAUSE and not partie.STOP:
        #             if self.CHOICE == 2:
        #                 if Loop_count % 40 == 0:
        #                     if Loop_count % 200 == 0:
        #                             partie.Slow_Down()
        #                     if partie.Slow_On:
        #                         partie.Slow_counter()
        #                         if partie.Slow_count % 2 == 0:
        #                             partie.mouv_ennemie()
        #                             partie.spawn ()
        #                     if not partie.Slow_On:
        #                             partie.mouv_ennemie()
        #                             partie.spawn ()
        #                     for _ in range(int(Loop_count/800)):
        #                         partie.spawn ()
        #             if self.CHOICE == 3:
        #                 if Loop_count % 25 == 0:
        #                     for _ in range(int(Loop_count/500)):
        #                         partie.spawn ()
        #                     if Loop_count % 125 == 0:
        #                         partie.Slow_Down()
        #                     if partie.Slow_On:
        #                         partie.Slow_counter()
        #                         if partie.Slow_count % 2 == 0:
        #                             partie.mouv_ennemie()
        #                             partie.spawn ()
        #                     if not partie.Slow_On:
        #                         partie.mouv_ennemie()
        #                         partie.spawn ()
        #             if self.CHOICE == 4:
        #                 if Loop_count % 15 == 0:
        #                     for _ in range(int(Loop_count/300)):
        #                         partie.spawn ()
        #                     if Loop_count % 75 == 0:
        #                         partie.Slow_Down()
        #                     if partie.Slow_On:
        #                         partie.Slow_counter()
        #                         if partie.Slow_count % 2 == 0:
        #                             partie.mouv_ennemie()
        #                             partie.spawn ()
        #                     if not partie.Slow_On:
        #                         partie.mouv_ennemie()
        #                         partie.spawn ()
        #         if not self.PAUSE and partie.stop_counter != 0:
        #             if Loop_count % 15 == 0:
        #                 partie.stop()
        #         if not self.PAUSE and partie.Kame_counter != 0:
        #             if Loop_count % 15 == 0:
        #                 partie.Kame_count()
                    
                
                pygame.display.update()
                end1 = time.perf_counter()


def leaderboard():
    run = True
    while run:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        PEPESUS = Button(base_image=pygame.image.load("Images\orange_button.png"), position=(640,250),
                        text_input="PepeSus", font=get_font(45), base_color="#d7fcd4", hovering_color="white")

        PEPETAG = Button(base_image=pygame.image.load("Images\purple_button.png"), position=(640,400),
                        text_input="PepeTag", font=get_font(45), base_color="#d7fcd4", hovering_color="white")

        PLAY_BACK = Button(base_image=None, position=(30, 20), 
                            text_input="BACK", font=get_font(10), base_color="White", hovering_color="Green")
        
        for button in [PEPESUS, PEPETAG, PLAY_BACK]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(MOUSE_POS):
                    run = False
                    break
                elif PEPESUS.checkForInput(MOUSE_POS):
                    pepeSus_Main.leaderboard(SCREEN)
                elif PEPETAG.checkForInput(MOUSE_POS): pass
                    #PepeTag_Main.leaderboard(SCREEN)
        pygame.display.update()
    
def select_profile():
    
    OPTION_BACK = Button(base_image=None, position=(30, 20), 
                            text_input="BACK", font=get_font(10), base_color="Black", hovering_color="Green")
    DONE_TEXT = get_font(32).render("Done", True, "#b68f40")
    DONE_RECT = DONE_TEXT.get_rect(center=(640,100))
    
    DONE_BUTTON = Button(base_image=pygame.transform.scale(pygame.image.load("Images\green.png"), (DONE_RECT.width, DONE_RECT.height)), position= (540-DONE_RECT.width/2,100+DONE_RECT.height/2), 
                        text_input="Done", font=get_font(15), base_color="Black", hovering_color="White")
    knife_img = pygame.transform.scale(pygame.image.load("Images\AmongUsCharacters\AmongUsKnife.png"), (84,84))
    images = []
    characters_buttons = []
    for i in range(2):
        for j in range(int(len(utility.COLORS)/2)):
            color = utility.COLORS[i*int(len(utility.COLORS)/2) + j]
            img = pygame.transform.scale(pygame.image.load(f"Images\AmongUsCharacters\{color}.png"), (84,84))
            position = (int(utility.WINDOW_DIM[0]/4) + img.get_height()*j, int(utility.WINDOW_DIM[1]/1.5)+img.get_width()*i)
            
            characters_buttons.append(Button(base_image=img, position=(position[0] + img.get_width()/2, position[1] + img.get_height()/2), 
                            text_input=None, font=get_font(10), base_color="Black", hovering_color="Green",
                            hovering_image=knife_img))
            images.append([color, img, position])
            

    color_selected = "Red"
    
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(540, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        PROFILE_MOUSE_POSITION = pygame.mouse.get_pos()
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                elif OPTION_BACK.checkForInput(PROFILE_MOUSE_POSITION) or DONE_BUTTON.checkForInput(PROFILE_MOUSE_POSITION):
                    done = True
                    break
                else:
                    active = False # Change the current color of the input box.
                    for char, button in zip(images, characters_buttons):
                        if button.checkForInput(PROFILE_MOUSE_POSITION):
                            color_selected = char[0]

                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        active = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                color = color_active if active else color_inactive

        SCREEN.fill((255,255,255))
        SCREEN.blit(DARK_HERMIT, (780, 220))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        SCREEN.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(SCREEN, color, input_box, 2)

        players = profile.get_profiles()
        i = 1
        for player in players:
            if text == player['id'][0:len(text)] and len(text) > 0:
                sub_input_box = pygame.Rect(540, 100, 140, 32)
                sub_surface = font.render(player['id'], True, color)
                sub_input_box.w = width
                SCREEN.blit(sub_surface, (sub_input_box.x+5, sub_input_box.y+5+i*32))
                i+=1
        
        for img in images:
            SCREEN.blit(img[1], img[2])

        for img, button in zip(images, characters_buttons):
            button.changeColor(PROFILE_MOUSE_POSITION)
            button.changeImage(PROFILE_MOUSE_POSITION)
            button.update(SCREEN)
            if color_selected == img[0]:
                SCREEN.blit(knife_img, (img[2]))

        for button in [OPTION_BACK, DONE_BUTTON]:
            button.changeColor(PROFILE_MOUSE_POSITION)
            button.changeImage(PROFILE_MOUSE_POSITION)
            button.update(SCREEN)
        
        
        pygame.display.flip()

    return profile.Profile(text) if len(text) > 0 else None, color_selected



def main_menu():
    profile_joueur = (None, "Red")
    run = True
    while run:
        #Fond blanc
        SCREEN.fill("white")

        #end les infos de la position de la souris
        MENU_MOUSE_POSITION = pygame.mouse.get_pos()

        #Texte + boite de texte("hitbox")
        MENU_TEXT = get_font(100).render("Main menu", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640,100))
        

        PLAY_BUTTON = Button(base_image=pygame.image.load("Images\green_button.png"), position=(640,250),
                        text_input="PLAY", font=get_font(45), base_color="#d7fcd4", hovering_color="white")

        QUIT_BUTTON = Button(base_image=pygame.image.load("Images\Black_Button.png"), position=(640,550),
                        text_input="QUIT", font=get_font(45), base_color="#d7fcd4", hovering_color="white")

        LEADERBOARD_BUTTON = Button(base_image=I.LEADERBOARD, position=(1260,700),
                            text_input="", font=get_font(0), base_color="#d7fcd4", hovering_color="white", hovering_image=I.LEADERBOARD_H)
        PROFILE_BUTTON = Button(base_image=I.PROFILE, position=(1220,700),
                            text_input="", font=get_font(0), base_color="#d7fcd4", hovering_color="white", hovering_image=I.PROFILE_H)
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON, LEADERBOARD_BUTTON, PROFILE_BUTTON]:
            button.changeColor(MENU_MOUSE_POSITION)
            button.changeImage(MENU_MOUSE_POSITION)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POSITION):
                    play(profile_joueur)
                elif LEADERBOARD_BUTTON.checkForInput(MENU_MOUSE_POSITION):
                    leaderboard()
                elif PROFILE_BUTTON.checkForInput(MENU_MOUSE_POSITION):
                    profile_joueur = select_profile()
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POSITION):
                    run = False
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()
main_menu()