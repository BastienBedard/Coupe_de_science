import numpy as np
import random as rd
import pygame


class SpaceAdventure():
    def __init__(self, niveau):
        self.tableau = self.niveau(niveau)

        self.vaisseau = pygame.image.load("Images\Vaisseau.png")
        self.vaisseau = pygame.transform.scale(self.vaisseau, (32,32))
        
        self.PepeTagPlay_BG = pygame.image.load("Images\BackgroundMenu.png")
        self.PepeTagPlay_BG = pygame.transform.scale(self.PepeTagPlay_BG, (1280,720))
        
        self.gold = pygame.image.load("Images\Piere6.png")
        self.gold = pygame.transform.scale(self.gold, (32,32))
        
        self.Window_Size = (1280, 720)
        self.goldcount = 0
        self.end = False
    
    def get_font(self, size):
        return pygame.font.Font("fonts/font1.ttf", size)
    
    def niveau(self, niveau):
        if niveau == 1:
            taille = 7
            tableau = np.zeros((taille, taille))
            self.taille = taille
            tableau[6][3] = 1
            tableau[2:6,3] = 2
        return tableau
    
    def avant(self):
        posi = np.where(self.tableau == 1)
        self.tableau[posi[0][0]][posi[1][0]] = 0
        self.tableau[posi[0][0]-1][posi[1][0]] = self.move('vaisseau', self.tableau[posi[0][0]-1][posi[1][0]])
        
    def move(self, who, position):
        if who == 'vaisseau':
            if position == 0:
                position = 1
            if position == 2:
                self.goldcount += 1
                position = 1
        return position

    def displayScreen(self, screen):
        square_dim = int(self.Window_Size [0] /40)
        square = pygame.Surface((square_dim,square_dim))
        bigsquare = pygame.Surface((square_dim*2,square_dim*2))
        screen.blit(self.PepeTagPlay_BG, (0, 0))

        coord_x = self.Window_Size[0]/2 - (int(self.taille/2))*square_dim
        coord_y = self.Window_Size[1]/2 - (int(self.taille/2))*square_dim
        
        for ligne in self.tableau:
            for point in  ligne:
                if point == 1:
                    screen.blit(self.vaisseau, (coord_x,coord_y))
                elif point == 2:
                    screen.blit(self.gold, (coord_x,coord_y))
                coord_x += square_dim
            coord_x = self.Window_Size[0]/2 - (int(self.taille/2))*square_dim
            coord_y += square_dim
        coord_x = self.Window_Size[0]/2 - (int(self.taille/2))*square_dim
        coord_y = self.Window_Size[1]/2 - (int(self.taille/2))*square_dim
        
        for i in range(self.taille+1):
            pointX = coord_x + (i)*square_dim
            pygame.draw.line(screen, (224,224,224), (pointX,coord_y),(pointX,coord_y + (self.taille)*square_dim))
        for j in range(self.taille+1):
            pointY = coord_y + (j)*square_dim
            pygame.draw.line(screen, (224,224,224), (coord_x, pointY),(coord_x + (self.taille)*square_dim, pointY))
