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
def play(equipe, niveau, moves):
    if True:
        partie = SpaceAdventure(niveau)
        start = time.perf_counter()
        end1 = time.perf_counter()
        
        strmoves = longmoves(moves)
        run = True
        # turn_count = 0
        Loop_count = 0
        move_count = 0
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

                if (Loop_count + 1) % 35 == 1:
                    partie.posi_vaisseau()
                    if len(np.where(partie.tableau == 5)[0]) == 0:
                        run = False
                    elif partie.mort:
                        run = False
                    else:
                        partie.action(strmoves[move_count])
                    move_count += 1
                
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

def longmoves(moves):
    strmoves = []
    for move in moves:
        if type(move) is str:
            strmoves += [move]
        elif type(move) is list:
            for i in range(move[0]):
                strmoves += move[1:]
    return strmoves



def main_menu(equipe, niveau, moves):
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

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
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
                    play(equipe = equipe, niveau = niveau, moves = moves)
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POSITION):
                    run = False
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()



equipe = 1
niveau = 2
moves = [[2,'avant'], 'tdroite', 'avant', 'Avant', 'avant', 'tdroite', 'Avant']

main_menu(equipe, niveau, moves)