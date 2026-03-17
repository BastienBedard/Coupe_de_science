import numpy as np
import pygame


class SpaceAdventure():
    """
        Class that control the game board and displays the current state of the game. 
    """
    def __init__(self, niveau: int):
        self.niveau = niveau
        self.tableau, self.taille, self.scalesize = self.niveau_choice()
        self.Window_Size = (1280, 720)
        
        self.vaisseau = pygame.image.load("Images/Images_2026/vaisseau2.png")
        self.vaisseau = pygame.transform.scale(self.vaisseau, (self.scalesize, self.scalesize))
        self.vaisseauD = pygame.transform.rotate(self.vaisseau, 270)
        self.vaisseauG = pygame.transform.flip(self.vaisseauD, True, False)
        self.vaisseauR = pygame.transform.rotate(self.vaisseau, 180)

        self.obstacle = pygame.image.load("Images/Images_2026/portal.png")
        self.obstacle = pygame.transform.scale(self.obstacle, (self.scalesize, self.scalesize))
        
        self.little_screen = pygame.image.load("Images/Images_2026/small_BG.png")
        self.little_screen = pygame.transform.scale(self.little_screen, (self.scalesize*(self.taille-2), self.scalesize*(self.taille-2)))

        self.Kaboom = pygame.image.load("Images/Images_2026/death.png")
        self.Kaboom = pygame.transform.scale(self.Kaboom, (self.scalesize, self.scalesize))

        self.Background = pygame.image.load("Images/Images_2026/Background.jpg")
        self.Background = pygame.transform.scale(self.Background, self.Window_Size)

        self.gold = pygame.image.load("Images/Images_2026/Sphere_energie.png")
        self.gold = pygame.transform.scale(self.gold, (self.scalesize, self.scalesize))

        self.goldcount = 0
        self.mort = False
        self.fini = False
        self.end = False

    def get_font(self, size: int):
        return pygame.font.Font("Fonts/font1.ttf", size)

    def initable(self, taille: int):
        table = np.zeros((taille, taille))
        table[0] = 7
        table[taille-1] = 7
        table[:,0] = 7
        table[:,taille-1] = 7
        return table

    def niveau_choice(self):
        if self.niveau == 0:
            scalesize = 90
            taille = 7
            tableau = self.initable(taille)
            tableau[5][3] = 1
            tableau[1:5,3] = 5
            tableau[2][2] = 6
            tableau[4][2] = 6
            tableau[2][4] = 6
            tableau[4][4] = 6
        elif self.niveau == 1:
            scalesize = 90
            taille = 7
            tableau = self.initable(taille)
            tableau[5][2] = 1
            tableau[2][3] = 6
            tableau[5][5] = 6
            tableau[3][4] = 6
            tableau[1][1] = 6
            tableau[3][1] = 6
            tableau[4,3:5] = 5
            tableau[2:4,5] = 5
        elif self.niveau == 2:
            scalesize = 70
            taille = 9
            tableau = self.initable(taille)
            tableau[7, 1] = 1
            tableau[2][3] = 5
            tableau[2][5] = 5
            tableau[6, 3:5] = 5
            tableau[3:5, 2] = 5
            tableau[3:5, 6] = 5
            tableau[3][3] = 6
            tableau[5][4] = 6
            tableau[4][5] = 6
            tableau[3][4] = 6
            tableau[1][6] = 6
            tableau[5][7] = 6
            tableau[7][3] = 6
        elif self.niveau == 3:
            scalesize = 70
            taille = 9
            tableau = self.initable(taille)
            tableau[7][4] = 1
            tableau[1:6, 4] = 5
            tableau[3][3] = 5
            tableau[5][3] = 5
            tableau[3][4] = 0
            tableau[2][7] = 6
            tableau[4][7] = 6
            tableau[3,6:8] = 6
            tableau[4][3] = 6
            tableau[6][3] = 6
            tableau[6][1] = 6
            tableau[1][3] = 6
            tableau[2][2] = 6
            tableau[7][3] = 5
        elif self.niveau == 4:
            scalesize = 55
            taille = 11
            tableau = self.initable(taille)
            tableau[1][5] = 2
            tableau[2:10:2, 3:9:2] = 5
            tableau[3:9:2, 4:8:2] = 6
        else:
            scalesize = 55
            taille = 11
            tableau = self.initable(taille)
            tableau[1:11:2, 1:11:2] = 5
            tableau[2:10:2, 2:10:2] = 5
            tableau[2:10:2, 1:11:2] = 6
            tableau[1:11:2, 2:10:2] = 6
            tableau[5, 5] = 1
        return tableau, taille, scalesize

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
            self.goldcount += 50
            position = who
        elif position in (6, 7):
            position = 8
        return position

    def displayScreen(self, screen):
        square_dim = self.scalesize
        screen.blit(self.Background, (0, 0))

        coord_x = self.Window_Size[0]/2 - (int(self.taille/2))*square_dim
        coord_y = self.Window_Size[1]/2 - (int(self.taille/2))*square_dim
        screen.blit(self.little_screen, (coord_x+square_dim, coord_y+square_dim))

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
                    screen.blit(self.obstacle, (coord_x,coord_y))
                elif point == 8:
                    screen.blit(self.Kaboom, (coord_x,coord_y))
                coord_x += square_dim
            coord_x = self.Window_Size[0]/2 - (int(self.taille/2))*square_dim
            coord_y += square_dim
        coord_x = self.Window_Size[0]/2 - (int(self.taille/2)-1)*square_dim
        coord_y = self.Window_Size[1]/2 - (int(self.taille/2)-1)*square_dim

        for i in range(self.taille-1):
            pointX = coord_x + (i)*square_dim
            pygame.draw.line(screen, (224,224,224),
                                (pointX,coord_y),(pointX,coord_y + (self.taille-2)*square_dim))
        for j in range(self.taille-1):
            pointY = coord_y + (j)*square_dim
            pygame.draw.line(screen, (224,224,224),
                                (coord_x, pointY),(coord_x + (self.taille-2)*square_dim, pointY))
