import pygame

class Button():
    def __init__(self, colour_theme, rect, font, finish_event = None, parent = None, text = '', max_activations = None, activation_dict = {}):
        self.colour_theme = colour_theme
        self.rect = pygame.Rect(rect)
        self.border = pygame.Rect(rect[0] - 2, rect[1] - 2, rect[2] + 4, rect[3] + 4)
        self.font = font
        self.hovered = False
        self.clicked = False
        self.parent = parent
        self.text = text
        self.text_image = self.font.render(self.text, 1, self.colour_theme.text)
        self.finish_event = finish_event
        self.max_activations = max_activations
        self.activations = 0

    def draw(self, win):
        colour = self.colour_theme.active
        if not self.finish_event.valid():
            colour = self.colour_theme.inactive
        elif self.clicked:
            colour = self.colour_theme.click
        elif self.hovered:
            colour = self.colour_theme.hover
        pygame.draw.rect(win, self.colour_theme.border, self.border, 0)
        pygame.draw.rect(win, colour, self.rect, 0)
        win.blit(self.text_image, self.text_image.get_rect(center = self.rect.center))

    def finish(self):
        if self.finish_event.valid():
            self.finish_event()
            self.activations += 1
            if self.max_activations is not None and self.activations >= self.max_activations:
                self.deactivate()

    def click(self):
        self.finish()

    def activate(self):
        if self not in self.parent:
            self.parent + self
        self.parent.move_buttons()

    def deactivate(self):
        self.parent.list.remove(self)
        self.parent.move_buttons()

    def move_button(self, x, y, w, h):
        self.rect.update(x, y, w, h)
        self.border.update(x - 1, y - 1, w + 2, h + 2)

class Button_Toggle(Button):
    def __init__(self, colour_theme, rect, font, complete_amount, progress_tick = 0, finish_event = None, start_event = None, progress_event = None, parent = None, text = '', max_activations = None):
        super().__init__(colour_theme, rect, font, parent= parent, text= text, finish_event = finish_event, max_activations = max_activations)
        self.active = False
        self.started = False
        self.complete_amount = complete_amount
        self.progress_tick = progress_tick
        self.progress = 0
        self.start_event = start_event
        self.progress_event = progress_event

    def draw(self, win):
        colour = self.colour_theme.active
        bar_colour = self.colour_theme.bar
        bar = (self.rect[0], self.rect[1], self.rect[2] * self.progress / self.complete_amount, self.rect[3])
        if not (self.start_event.valid() and self.progress_event.valid()):
            colour = self.colour_theme.inactive
            bar_colour = self.colour_theme.bar_inactive  
        elif self.clicked:
            colour = self.colour_theme.click
            bar_colour = self.colour_theme.hover
        elif self.hovered or self.active:
            colour = self.colour_theme.hover
            bar_colour = self.colour_theme.active
        pygame.draw.rect(win, self.colour_theme.border, self.border, 0)
        pygame.draw.rect(win, colour, self.rect, 0)
        pygame.draw.rect(win, bar_colour, bar, 0)
        win.blit(self.text_image, self.text_image.get_rect(center = self.rect.center))

    def click(self):
        if self.active:
            self.active = False
            return
        if not self.started:
            if self.start_event.valid() and self.progress_event.valid():
                self.start_event()
                self.started = True
                self.active = True
                return
        else:
            if self.progress_event.valid():
                self.active = True

    def tick(self):
        if not self.progress_event.valid():
            self.active = False
            return
        self.progress_event()
        self.progress += self.progress_tick
        if self.progress >= self.complete_amount:
            self.finish()
            self.progress = 0
            self.active = False
            self.started = False
            self.click()

    def prog(self, int):
        self.progress += int