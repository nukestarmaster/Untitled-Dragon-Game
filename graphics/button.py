import pygame

class Button():
    def __init__(self, colour, colour_pressed, x, y, h, w, font, active = False, parent = None, text = '', button_event = None):
        self.colour = colour
        self.colour_pressed = colour_pressed
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.active = active
        self.parent = parent
        self.text = text
        self.text_image = self.font.render(self.text, 1, 'black')
        self.button_event = button_event
        if self.parent is not None:
            parent.add_child(self)

    def draw(self, win, pressed = False):
        if not self.active:
            return
        colour = self.colour
        if pressed:
            colour = self.colour_pressed
        pygame.draw.rect(win, colour, self.rect, 0)
        win.blit(self.text_image, self.text_image.get_rect(center = self.rect.center))

    def click(self):
        self.button_event()

    def activate(self):
        self.active = True

    