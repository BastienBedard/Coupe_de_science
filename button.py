import pygame

class Button:
    def __init__(self, base_image, position, text_input, font, base_color, hovering_color, hovering_image=None):

        self.hovering_image, self.base_image = hovering_image, base_image
        self.image = self.base_image

        self.x = position[0]
        self.y = position[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        if hovering_image is None:
            self.hovering_image = self.base_image
        self.rect = self.image.get_rect(center=(self.x, self.y))
        if self.image is None and self.text_input is None:
            self.rect = self.hovering_image.get_rect(center=(self.x, self.y))
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def changeImage(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.image = self.hovering_image
        else:
            self.image = self.base_image
