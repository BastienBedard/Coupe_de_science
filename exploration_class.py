import numpy as np
import pygame


class SpaceAdventure():
    """
        Class that control the game board and displays the current state of the game. 
    """
    def __init__(self, niveau: int):
        self.tableau = self.niveau(niveau)

        self.vaisseau = pygame.image.load("Images\Vaisseau.png")
        self.vaisseau = pygame.transform.scale(self.vaisseau, (64,64))
        self.vaisseauD = pygame.transform.rotate(self.vaisseau, 270)
        self.vaisseauG = pygame.transform.rotate(self.vaisseau, 90)
        self.vaisseauR = pygame.transform.rotate(self.vaisseau, 180)

        self.meteor = pygame.image.load("Images\météorites.png")
        self.meteor = pygame.transform.scale(self.meteor, (64,64))

        self.Kaboom = pygame.image.load("Images\Kaboom.png")
        self.Kaboom = pygame.transform.scale(self.Kaboom, (64,64))

        self.PepeTagPlay_BG = pygame.image.load("Images\BackgroundMenu.png")
        self.PepeTagPlay_BG = pygame.transform.scale(self.PepeTagPlay_BG, (1280,720))

        self.gold = pygame.image.load("Images\Piere6.png")
        self.gold = pygame.transform.scale(self.gold, (64,64))

        self.Window_Size = (1280, 720)
        self.goldcount = 0
        self.mort = False
        self.fini = False
        self.end = False

    def get_font(self, size: int):
        return pygame.font.Font("fonts/font1.ttf", size)

    def initable(self, taille: int):
        table = np.zeros((taille, taille))
        table[0] = 6
        table[taille-1] = 6
        table[:,0] = 6
        table[:,taille-1] = 6
        return table

    def niveau(self, niveau: int):
        if niveau == 1:
            taille = 7
            self.taille = taille
            tableau = self.initable(taille)
            tableau[5][3] = 1
            tableau[1:5,3] = 5
        elif niveau == 2:
            taille = 7
            tableau = self.initable(taille)
            self.taille = taille
            tableau[5][2] = 1
            tableau[3:5,2] = 5
            tableau[2][2] = 6
            tableau[3,2:6] = 5
            tableau[2][5] = 5
        elif niveau == 3:
            taille = 9
            self.taille = taille
            tableau = self.initable(taille)
            tableau[7, 1] = 1
            tableau[2, 2:7] = 5
            tableau[6, 2:7] = 5
            tableau[2:7, 2] = 5
            tableau[2:7, 6] = 5
        elif niveau == 4:
            taille = 9
            self.taille = taille
            tableau = self.initable(taille)
            tableau[7][4] = 1
            tableau[1:7, 4] = 5
            tableau[3][3] = 5
            tableau[5][3] = 5
            tableau[2][3] = 6
            tableau[4][3] = 6
            tableau[6][3] = 6
        return tableau

    def posi_vaisseau(self):
        posi1 = np.where(self.tableau == 1)
        posi2 = np.where(self.tableau == 2)
        posi3 = np.where(self.tableau == 3)
        posi4 = np.where(self.tableau == 4)
        if len(posi1[0]) !=0:
            val = 1
            positrue = posi1
        elif len(posi2[0]) !=0:
            val = 2
            positrue = posi2
        elif len(posi3[0]) !=0:
            val = 3
            positrue = posi3
        elif len(posi4[0]) !=0:
            val = 4
            positrue = posi4
        else:
            self.mort = True
            return False
        return val, positrue

    def action(self, strmove: list):
        if strmove in ['avant', 'Avant']:
            self.avant()
        elif strmove in ['tdroite','Tdroite']:
            self.tourner_D()
        elif strmove in ['tgauche','Tgauche']:
            self.tourner_G()

    def avant(self):
        val, posi = self.posi_vaisseau()
        self.tableau[posi[0][0]][posi[1][0]] = 0
        if val == 1:
            self.tableau[posi[0][0]-1][posi[1][0]] = self.move(1,
                                                    self.tableau[posi[0][0]-1][posi[1][0]])
        elif val == 2:
            self.tableau[posi[0][0]][posi[1][0]+1] = self.move(2,
                                                    self.tableau[posi[0][0]][posi[1][0]+1])
        elif val == 3:
            self.tableau[posi[0][0]+1][posi[1][0]] = self.move(3,
                                                    self.tableau[posi[0][0]+1][posi[1][0]])
        elif val == 4:
            self.tableau[posi[0][0]][posi[1][0]-1] = self.move(4,
                                                    self.tableau[posi[0][0]][posi[1][0]-1])

    def tourner_D(self):
        val, posi = self.posi_vaisseau()
        self.tableau[posi[0][0]][posi[1][0]] = int((val % 4) + 1)

    def tourner_G(self):
        val, posi = self.posi_vaisseau()
        if val == 1:
            val = 5
        self.tableau[posi[0][0]][posi[1][0]] = val-1

    def move(self, who: int, position: int):
        if position == 0:
            position = who
        elif position == 5:
            self.goldcount += 1
            position = who
        elif position == 6:
            position = 7
        return position

    def displayScreen(self, screen):
        square_dim = int(self.Window_Size [0] /20)
        # square = pygame.Surface((square_dim,square_dim))
        screen.blit(self.PepeTagPlay_BG, (0, 0))

        coord_x = self.Window_Size[0]/2 - (int(self.taille/2))*square_dim
        coord_y = self.Window_Size[1]/2 - (int(self.taille/2))*square_dim

        for ligne in self.tableau:
            for point in  ligne:
                if point == 1:
                    screen.blit(self.vaisseau, (coord_x,coord_y))
                elif point == 2:
                    screen.blit(self.vaisseauD, (coord_x,coord_y))
                elif point == 3:
                    screen.blit(self.vaisseauR, (coord_x,coord_y))
                elif point == 4:
                    screen.blit(self.vaisseauG, (coord_x,coord_y))
                elif point == 5:
                    screen.blit(self.gold, (coord_x,coord_y))
                elif point == 6:
                    screen.blit(self.meteor, (coord_x,coord_y))
                elif point == 7:
                    screen.blit(self.Kaboom, (coord_x,coord_y))
                coord_x += square_dim
            coord_x = self.Window_Size[0]/2 - (int(self.taille/2))*square_dim
            coord_y += square_dim
        coord_x = self.Window_Size[0]/2 - (int(self.taille/2))*square_dim
        coord_y = self.Window_Size[1]/2 - (int(self.taille/2))*square_dim

        for i in range(self.taille+1):
            pointX = coord_x + (i)*square_dim
            pygame.draw.line(screen, (224,224,224),
                                (pointX,coord_y),(pointX,coord_y + (self.taille)*square_dim))
        for j in range(self.taille+1):
            pointY = coord_y + (j)*square_dim
            pygame.draw.line(screen, (224,224,224),
                                (coord_x, pointY),(coord_x + (self.taille)*square_dim, pointY))
