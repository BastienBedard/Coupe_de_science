"""Blah Blah Blah"""

import os
import sys
import time
import pygame
import numpy as np
from button import Button
from utility import images
from exploration_class import SpaceAdventure
from gestion_scores import write, read


I = images()
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

#Initialisation de Pygame
pygame.init()

#Size/Resolution de la window
SCREEN = pygame.display.set_mode((1280,720), pygame.SCALED)
pygame.display.toggle_fullscreen()
pygame.display.set_caption("Jeux")

#Font personnalisé
def get_font(size: int):
    """ Initialize a font object with the right size.

    Args:
        size (int): the size of the font.

    Returns:
        font?: An font object.
    """
    return pygame.font.Font("Fonts/Lato-Regular.ttf", size)

# Gestion de tout l'interface de jeu.
def play(equipe: int, niveau: int, moves: list, number_of_frames: int = 15, time_interval: float = 0.1):
    """ Function that leads the whole game.

    Args:
        equipe (int): Le numéro de l'équipe qui joue.
        niveau (int): Le niveau jouer.
        moves (list): La liste des coups pour le niveau.
    """
    partie = SpaceAdventure(niveau)
    
    number_of_frames_init = number_of_frames

    FAST_MODES = 4
    fast_mode = 1
    start_time = time.perf_counter()
    endtime = time.perf_counter()
    fin = False
    pause = True
    
    best_score = [300, 300, 700, 450, 700]
    strmoves, level_score = longmoves(moves, niveau)
    
    type_fin = 'Erreur'
    Loop_count = 0
    move_count = 0
    run = True
    while run:
        # slow down the loop
        endtime = time.perf_counter()
        if (endtime - start_time) >= time_interval:
            Loop_count += 1

            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            partie.displayScreen(SCREEN)

            # Condition to do the next move.
            if (Loop_count) % (number_of_frames) == 0 and not fin and not pause:
                partie.posi_vaisseau()
                if partie.mort:
                    # Le vaisseau a crash dans les météorites.
                    fin = True
                    type_fin = 'Vous êtes mort !'
                else:
                    if move_count == len(strmoves):
                        # Tous les moves ont été fait.
                        fin = True
                        type_fin = "Vous n'avez pas récolté tous les minerais"
                        if len(np.where(partie.tableau == 5)[0]) == 0:
                            # Toutes les minerais ont été récolté.
                            level_score += 100
                            type_fin = 'Félicitation, vous avez réussi !'
                    else:
                        # Si tout est ok on fait le prochain move.
                        partie.action(strmoves[move_count])
                if fin:
                    # Calcul les scores à la fin.
                    level_score += partie.goldcount
                    level_score = int(1000*level_score/best_score[niveau])
                    write(equipe=equipe, level=niveau, score=level_score)
                move_count += 1

            if fin:
                MORT_FOND = pygame.Surface((1200, 145))
                MORT_FOND_RECT = MORT_FOND.get_rect(center=(640, 100))
                MORT_TEXT = get_font(45).render(type_fin, True, "#b68f40")
                MORT_RECT = MORT_TEXT.get_rect(center=(640, 100))
                SCORE_TEXT = get_font(25).render(f'Votre score pour ce niveau est : {level_score}',
                                                    True, "#b68f40")
                SCORE_RECT = SCORE_TEXT.get_rect(center=(640, 135))
                SCREEN.blit(MORT_FOND, MORT_FOND_RECT)
                SCREEN.blit(MORT_TEXT, MORT_RECT)
                SCREEN.blit(SCORE_TEXT, SCORE_RECT)

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

            # Boutton pour mettre le jeu en pause
            pause_text_input = 'Play'
            if not pause:
                pause_text_input = 'Pause'
            PAUSE = Button(base_image=pygame.Surface((200, 100)), position=(200, 350),
                                text_input=pause_text_input, font=get_font(65),
                                base_color="#b68f40", hovering_color="Green")
            PAUSE.changeColor(PLAY_MOUSE_POS)
            PAUSE.update(SCREEN)

            # Boutton pour quitter le jeu
            QUIT = Button(base_image=pygame.Surface((200, 100)), position=(1100, 350),
                                    text_input="Quitter", font=get_font(55), base_color="#b68f40",
                                    hovering_color="Green")
            QUIT.changeColor(PLAY_MOUSE_POS)
            QUIT.update(SCREEN)
            
            # Boutton pour changer la vitesse du jeu
            fast_text_input = f"x{fast_mode} >>"
            if fast_mode == FAST_MODES:
                fast_text_input = "MAX >>"
            FAST = Button(base_image=pygame.Surface((200, 100)), position=(200, 550),text_input=fast_text_input, font=get_font(55), base_color="#b68f40",hovering_color="Green")
            FAST.changeColor(PLAY_MOUSE_POS)
            FAST.update(SCREEN)
            
            # Boutton pour rejouer le niveau
            REPLAY = Button(base_image=pygame.Surface((200, 100)), position=(1100, 550),text_input="Rejouer", font=get_font(55), base_color="#b68f40",hovering_color="Green")
            REPLAY.changeColor(PLAY_MOUSE_POS)
            REPLAY.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if PAUSE.checkForInput(PLAY_MOUSE_POS):
                            pause = not pause
                            if (not pause) and fin:
                                fin = False
                                partie = SpaceAdventure(niveau)
                                move_count = 0
                                Loop_count = 0
                                strmoves, level_score = longmoves(moves, niveau)
                        elif REPLAY.checkForInput(PLAY_MOUSE_POS):
                            pause = True
                            fin = False
                            partie = SpaceAdventure(niveau)
                            move_count = 0
                            Loop_count = 0
                            strmoves, level_score = longmoves(moves, niveau)
                        elif FAST.checkForInput(PLAY_MOUSE_POS):
                            fast_mode = (fast_mode) % FAST_MODES + 1
                            if fast_mode == FAST_MODES:
                                number_of_frames = 1
                            else:
                                number_of_frames = int(number_of_frames_init/(fast_mode))
                        elif QUIT.checkForInput(PLAY_MOUSE_POS):
                            run = False
                            break
            pygame.display.update()
            start_time = endtime

def recursive_moves(moves: list, strmoves: list):
    for i in range(moves[0]):
        for move in moves:
            if isinstance(move, str):
                strmoves += [move]
            elif isinstance(move, list):
                strmoves = recursive_moves(move, strmoves)
    return strmoves
    
def count_scores(moves:list):
    count = 0
    for move in moves:
        if isinstance(move, str):
            count += 1
        elif isinstance(move, list):
            count += count_scores(move)
    return count

def longmoves(moves: list, niveau: int):
    """ Calculate the score for the number of moves 
        and rewrite the loop as sequence of moves.

    Args:
        moves (list): A list of moves and loop of moves.

    Returns:
        strmoves (list): List with only string of moves.
        score (int): The score calculated.
    """
    best_solution = [1, 3, 5, 6, 8]
    if moves == ['']:
        raise ValueError("\n\n\n\n\n Aucune commande n'a été indiqué dans la liste de coups\n\n")
    strmoves = []
    best_score = best_solution[niveau]

    moves = [1] + moves
    strmoves = recursive_moves(moves, strmoves)
    score = best_score - count_scores(moves)
    
    return strmoves, score*10
