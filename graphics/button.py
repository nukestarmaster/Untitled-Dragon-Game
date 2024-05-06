import pygame

class Button():
    def __init__(self, colour_theme, x, y, h, w, font, button_event = None, parent = None, text = ''):
        self.colour_theme = colour_theme
        self.rect = pygame.Rect(x, y, w, h)
        self.border = pygame.Rect(x - 2, y - 2, w + 4, h + 4)
        self.font = font
        self.hovered = False
        self.clicked = False
        self.parent = parent
        self.text = text
        self.text_image = self.font.render(self.text, 1, self.colour_theme.text)
        self.button_event = button_event

    def draw(self, win):
        colour = self.colour_theme.active
        if not self.button_event.valid():
            colour = self.colour_theme.inactive
        elif self.clicked:
            colour = self.colour_theme.click
        elif self.hovered:
            colour = self.colour_theme.hover
        pygame.draw.rect(win, self.colour_theme.border, self.border, 0)
        pygame.draw.rect(win, colour, self.rect, 0)
        win.blit(self.text_image, self.text_image.get_rect(center = self.rect.center))

    def click(self):
        self.button_event()

    def activate(self):
        if self not in self.parent:
            self.parent.append(self)

    