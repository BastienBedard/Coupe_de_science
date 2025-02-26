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
        fin = False
        strmoves, level_score = longmoves(moves)
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

                if (Loop_count + 1) % 35 == 1 and not fin:
                    partie.posi_vaisseau()
                    if len(np.where(partie.tableau == 5)[0]) == 0:
                        fin = True
                    elif partie.mort:
                        fin = True
                    else:
                        if move_count == len(strmoves):
                            fin = True
                        else:
                            partie.action(strmoves[move_count])
                    if fin:
                        level_score += partie.goldcount
                    move_count += 1
                
                if fin:
                    MORT_FOND = pygame.image.load("Images\Large_black_button.png")
                    MORT_FOND_RECT = pygame.image.load("Images\Large_black_button.png").get_rect(center=(640, 300))
                    MORT_TEXT = get_font(45).render("Vous êtes mort!", True, "#b68f40")
                    MORT_RECT = MORT_TEXT.get_rect(center=(640, 300))
                    SCORE_TEXT = get_font(25).render(f'Votre score pour ce niveau est : {level_score}', True, "#b68f40")
                    SCORE_RECT = SCORE_TEXT.get_rect(center=(640, 335))
                    SCREEN.blit(MORT_FOND, MORT_FOND_RECT)
                    SCREEN.blit(MORT_TEXT, MORT_RECT)
                    SCREEN.blit(SCORE_TEXT, SCORE_RECT)

                    BACK_DEAD = Button(base_image=pygame.image.load("Images\Black_Button.png"), position=(640, 500), 
                                        text_input="OK...", font=get_font(35), base_color="#b68f40", hovering_color="Green")

                    BACK_DEAD.changeColor(PLAY_MOUSE_POS)
                    BACK_DEAD.update(SCREEN)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                                    run = False
                                    break
                                if BACK_DEAD.checkForInput(PLAY_MOUSE_POS):
                                    run = False
                                    break

                        pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                                run = False
                                break

                
                pygame.display.update()
                end1 = time.perf_counter()

def longmoves(moves):
    strmoves = []
    score = 30
    for move in moves:
        if type(move) is str:
            strmoves += [move]
            score -= 1
        elif type(move) is list:
            for i in range(move[0]):
                for move2 in move[1:]:
                    if type(move2) is str:
                        strmoves += [move2]
                        score -= 1
                    elif type(move2) is list:
                        for j in range(move2[0]):
                            for move3 in move2:
                                if type(move3) is str:
                                    strmoves += [move3]
                                    score -= 1
                                elif type(move3) is list:
                                    score -= len(move3)-1
                                    for i in range(move3[0]):
                                        strmoves += move3[1:]
    return strmoves, score



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


