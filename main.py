"""Blah Blah Blah"""

import os
import sys
import time
import pygame
import numpy as np
from button import Button
from exploration_class import SpaceAdventure
from gestion_scores import write, read

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
def play(equipe: int, niveau: int, moves: list, number_of_frames: int = 12, time_interval: float = 0.1):
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

    if niveau not in (0, 1, 2, 3, 4):
        niveau = 5
        pause = False
        fast_mode = FAST_MODES
        number_of_frames = 1
        moves = [[100, 'tdroite']]

    best_score = [500, 500, 700, 650, 900, 200]
    strmoves_init, level_score_init = longmoves(moves, niveau)
    strmoves = strmoves_init
    level_score = level_score_init
    total_score = 0

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
                    level_score -= 100
                else:
                    if move_count == len(strmoves):
                        # Tous les moves ont été fait.
                        fin = True
                        type_fin = "Vous n'avez pas tout récolté"
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
                    total_score = int(1000*level_score/best_score[niveau])
                    if niveau == 5 : total_score = 0
                    # total_score = level_score
                    write(equipe=equipe, level=niveau, score=total_score)
                    pause = True
                move_count += 1

            if fin:
                MORT_FOND = pygame.Surface((1200, 125))
                MORT_FOND_RECT = MORT_FOND.get_rect(center=(640, 75))
                SCREEN.blit(MORT_FOND, MORT_FOND_RECT)

                MORT_TEXT = get_font(45).render(type_fin, True, "#b68f40")
                MORT_RECT = MORT_TEXT.get_rect(center=(640, 80))
                SCREEN.blit(MORT_TEXT, MORT_RECT)

                SCORE_TEXT = get_font(25).render(f'Votre score pour ce niveau est : {total_score}',
                                                    True, "#b68f40")
                SCORE_RECT = SCORE_TEXT.get_rect(center=(640, 115))
                SCREEN.blit(SCORE_TEXT, SCORE_RECT)

                SCORE_FOND = pygame.Surface((320, 300))
                SCORE_RECT = SCORE_FOND.get_rect(center=(200, 280))
                SCREEN.blit(SCORE_FOND, SCORE_RECT)
                HS_TITLE_TEXT = get_font(35).render(f"Vos meilleurs scores", True, "#b68f40")
                HS_TITLE_RECT = HS_TITLE_TEXT.get_rect(center=(200, 150))
                SCREEN.blit(HS_TITLE_TEXT, HS_TITLE_RECT)
                for level in range(5):
                    HIGH_SCORE_TEXT = get_font(35).render(f"Niveau {level} : {read(equipe, level)}",
                                                                                    True, "#b68f40")
                    HIGH_SCORE_RECT = HIGH_SCORE_TEXT.get_rect(center=(200, 200+level*50))
                    SCREEN.blit(HIGH_SCORE_TEXT, HIGH_SCORE_RECT)

            BEHIND = pygame.Surface((900, 50))
            BEHIND_RECT = BEHIND.get_rect(center=(640, 40))

            TOTAL_SCORE_TEXT = get_font(35).render(f"Score total : {read(equipe=equipe)}", 
                                                                    True, "#b68f40")
            TOTAL_SCORE_RECT = TOTAL_SCORE_TEXT.get_rect(center=(355, 40))

            EQUIPE_TEXT = get_font(35).render(f"Équipe : {equipe}", True, "#b68f40")
            EQUIPE_RECT = EQUIPE_TEXT.get_rect(center=(655, 40))

            NIVEAU_TEXT = get_font(35).render(f"Niveau : {niveau}", True, "#b68f40")
            NIVEAU_RECT = NIVEAU_TEXT.get_rect(center=(955, 40))

            SCREEN.blit(BEHIND, BEHIND_RECT)
            SCREEN.blit(TOTAL_SCORE_TEXT, TOTAL_SCORE_RECT)
            SCREEN.blit(EQUIPE_TEXT, EQUIPE_RECT)
            SCREEN.blit(NIVEAU_TEXT, NIVEAU_RECT)

            # Boutton pour mettre le jeu en pause
            pause_text_input = 'Play'
            if not pause:
                pause_text_input = 'Pause'
            elif pause and fin:
                pause_text_input = 'Rejouer'
            PAUSE = Button(base_image=pygame.Surface((200, 100)), position=(1100, 250),
                                text_input=pause_text_input, font=get_font(55),
                                base_color="#b68f40", hovering_color="Green")
            PAUSE.changeColor(PLAY_MOUSE_POS)
            PAUSE.update(SCREEN)

            # Boutton pour changer la vitesse du jeu
            fast_text_input = f"x{fast_mode} >>"
            if fast_mode == FAST_MODES:
                fast_text_input = "MAX >>"
            FAST = Button(base_image=pygame.Surface((200, 100)),
                            position=(1100, 400),text_input=fast_text_input, 
                            font=get_font(55), base_color="#b68f40",hovering_color="Green")
            FAST.changeColor(PLAY_MOUSE_POS)
            FAST.update(SCREEN)

            # Boutton pour quitter le jeu
            QUIT = Button(base_image=pygame.Surface((200, 100)), position=(1100, 550),
                                    text_input="Quitter", font=get_font(55), base_color="#b68f40",
                                    hovering_color="Green")
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
                            if (not pause) and fin:
                                fin = False
                                partie = SpaceAdventure(niveau)
                                move_count = 0
                                Loop_count = 0
                                strmoves, level_score = strmoves_init, level_score_init
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
    for _ in range(moves[0]):
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
    best_solution = [1, 3, 4, 4, 7, 1]
    if moves == ['']:
        raise ValueError("\n\n\n\n\n Aucune commande n'a été indiqué dans la liste de coups\n\n")
    strmoves = []
    best_score = best_solution[niveau]

    moves = [1] + moves
    strmoves = recursive_moves(moves, strmoves)
    score = best_score - count_scores(moves)

    if score > 0:
        score = 0
    return strmoves, score*20+200
