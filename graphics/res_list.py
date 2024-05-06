import pygame


class Res_List():
    def __init__(self, list, x, y, w, h, background, font, seperation, colour):
        self.list = list
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, w, h)
        self.background = background
        self.font = font
        self.seperation = seperation
        self.colour = colour

    def draw(self, win):
        pygame.draw.rect(win, self.background, self.rect)
        for i in range(len(self.list)):
            text_image = self.font.render(str(self.list[i]), 1, self.colour)
            win.blit(text_image, (self.x, self.y + (self.seperation + (self.font.size(str(self.list[i])))[1]) * i))
