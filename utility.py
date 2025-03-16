import pygame
WINDOW_DIM = (1280, 720)



BG = pygame.transform.scale(pygame.image.load("Images/BackgroundMenu.png"), (int(WINDOW_DIM[0]/40), int(WINDOW_DIM[0]/40)))
LEADERBOARD = pygame.transform.scale(pygame.image.load("Images/leaderboard_logo.png"), (40,40))
LEADERBOARD_H = pygame.transform.scale(pygame.image.load("Images/leaderboard_logo_h.png"), (40,40))
PROFILE = pygame.transform.scale(pygame.image.load("Images/Profile_logo1.png"), (40,40))
PROFILE_H = pygame.transform.scale(pygame.image.load("Images/Profile_logo2.png"), (40,40))

class images():
    def __init__(self):
        self.BG = BG
        self.LEADERBOARD = LEADERBOARD
        self.PROFILE = PROFILE
        self.LEADERBOARD_H = LEADERBOARD_H
        self.PROFILE_H = PROFILE_H