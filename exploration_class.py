import numpy as np
import random as rd
import pygame


class jeutag():
    def __init__(self, taille):
        self.tableau1 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        self.tableau = np.zeros((taille, taille))
        self.taille = taille

        self.vaisseau = pygame.image.load("Images\Vaisseau.png")
        self.vaisseau = pygame.transform.scale(self.vaisseau, (32,32))
        
        self.PepeTagPlay_BG = pygame.image.load("Images\BackgroundMenu.png")
        self.PepeTagPlay_BG = pygame.transform.scale(self.PepeTagPlay_BG, (1280,720))
        
        self.Window_Size = (1280, 720)
        
        self.end = False

    def play(self):
        posi = np.where(self.tableau == 1)
        
    
    def get_font(self, size):
        return pygame.font.Font("fonts/font1.ttf", size)

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
                coord_x += square_dim
            coord_x = self.Window_Size[0]/2 - (int(self.taille/2))*square_dim
            coord_y += square_dim
        coord_x = self.Window_Size[0]/2 - (int(self.taille/2))*square_dim
        coord_y = self.Window_Size[1]/2 - (int(self.taille/2))*square_dim
        
        for k in range(len(self.List_Feu)):
            screen.blit(self.Feu, (self.Window_Size[0]/2 - (int(self.taille/2))*square_dim + self.List_Feu[k][1]*square_dim, self.Window_Size[1]/2 - (int(self.taille/2))*square_dim + self.List_Feu[k][0]*square_dim))
        self.Feu_count +=1
        if self.Feu_count > 4:
            self.Feu_count = 0
            self.List_Feu = []
        for i in range(self.taille+1):
            pointX = coord_x + (i)*square_dim
            pygame.draw.line(screen, (224,224,224), (pointX,coord_y),(pointX,coord_y + (self.taille)*square_dim))
        for j in range(self.taille+1):
            pointY = coord_y + (j)*square_dim
            pygame.draw.line(screen, (224,224,224), (coord_x, pointY),(coord_x + (self.taille)*square_dim, pointY))
