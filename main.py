import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from turtle import Screen, update
import pygame, sys
import time
from button import Button
from utility import images
I = images()

from exploration_class import SpaceAdventure
from Scores import write, read
import numpy as np

#Initialisation de Pygame
pygame.init()

#Size/Resolution de la window
SCREEN = pygame.display.set_mode((1280,720), pygame.FULLSCREEN)
pygame.display.set_caption("Jeux")


#Font personnalisé
def get_font(size):
    return pygame.font.Font("fonts/Lato-Regular.ttf", size)

#Liste des jeux
def play(equipe, niveau, moves):
    partie = SpaceAdventure(niveau)
    start = time.perf_counter()
    end1 = time.perf_counter()
    fin = False
    strmoves, level_score = longmoves(moves)
    run = True
    pause = True
    type_fin = 'Erreur'
    # turn_count = 0
    Loop_count = 0
    move_count = 0
    while run:
        if (int(end1-start+1) * 10) % 5 == 0:
            Loop_count += 1
            
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            
            partie.displayScreen(SCREEN)
            
            if (Loop_count + 1) % 35 == 1 and not fin and not pause:
                partie.posi_vaisseau()
                if len(np.where(partie.tableau == 5)[0]) == 0:
                    fin = True
                    type_fin = 'Félicitation, vous avez réussi !'
                elif partie.mort:
                    fin = True
                    type_fin = 'Vous êtes mort !'
                else:
                    if move_count == len(strmoves):
                        fin = True
                        type_fin = "Vous n'avez pas récolté tous les minerais"
                    else:
                        partie.action(strmoves[move_count])
                if fin:
                    level_score += partie.goldcount
                    write(equipe=equipe, level=niveau, score=level_score)
                move_count += 1
            
            if fin:
                MORT_FOND = pygame.Surface((1200, 145))
                MORT_FOND_RECT = MORT_FOND.get_rect(center=(640, 100))
                MORT_TEXT = get_font(45).render(type_fin, True, "#b68f40")
                MORT_RECT = MORT_TEXT.get_rect(center=(640, 100))
                SCORE_TEXT = get_font(25).render(f'Votre score pour ce niveau est : {level_score}', True, "#b68f40")
                SCORE_RECT = SCORE_TEXT.get_rect(center=(640, 135))
                SCREEN.blit(MORT_FOND, MORT_FOND_RECT)
                SCREEN.blit(MORT_TEXT, MORT_RECT)
                SCREEN.blit(SCORE_TEXT, SCORE_RECT)

            if pause:
                pause_text_input = 'Play'
            elif not pause:
                pause_text_input = 'Pause'
            
            BEHIND = pygame.Surface((900, 50))
            BEHIND_RECT = BEHIND.get_rect(center=(640, 53))
            
            HIGH_SCORE_TEXT = get_font(35).render(f"Meilleur score : {read(equipe=equipe, level=niveau)}", True, "#b68f40")
            HIGH_SCORE_RECT = HIGH_SCORE_TEXT.get_rect(center=(355, 50))

            EQUIPE_TEXT = get_font(35).render(f"Équipe : {equipe}", True, "#b68f40")
            EQUIPE_RECT = EQUIPE_TEXT.get_rect(center=(655, 50))
            
            NIVEAU_TEXT = get_font(35).render(f"Niveau : {niveau}", True, "#b68f40")
            NIVEAU_RECT = NIVEAU_TEXT.get_rect(center=(955, 50))
            
            SCREEN.blit(BEHIND, BEHIND_RECT)
            SCREEN.blit(HIGH_SCORE_TEXT, HIGH_SCORE_RECT)
            SCREEN.blit(EQUIPE_TEXT, EQUIPE_RECT)
            SCREEN.blit(NIVEAU_TEXT, NIVEAU_RECT)
            
            PAUSE = Button(base_image=pygame.Surface((200, 100)), position=(200, 350), 
                                text_input=pause_text_input, font=get_font(65), base_color="#b68f40", hovering_color="Green")

            PAUSE.changeColor(PLAY_MOUSE_POS)
            PAUSE.update(SCREEN)

            QUIT = Button(base_image=pygame.Surface((200, 100)), position=(1100, 350), 
                                    text_input="Quiter", font=get_font(55), base_color="#b68f40", hovering_color="Green")

            QUIT.changeColor(PLAY_MOUSE_POS)
            QUIT.update(SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if PAUSE.checkForInput(PLAY_MOUSE_POS):
                            pause = not pause
                        elif QUIT.checkForInput(PLAY_MOUSE_POS):
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
