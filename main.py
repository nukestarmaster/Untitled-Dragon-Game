import pygame
from graphics.button import Button, Button_Toggle
from graphics.button_list import Buttton_List
from graphics.colour_themes import Button_Theme
from graphics.res_list import Res_List
from logic.resource import Resource
from logic.event import Event
from sys import exit

width = 800
height = 600
framerate = 60
red_theme = Button_Theme('red', 'grey', (131, 0, 0), 'black', 'black', 'dark grey', (255, 63, 63), "white")
blue_theme = Button_Theme('blue', 'grey', (0, 0, 131), 'black', 'black', 'dark grey', (63, 63, 255), "white")

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Untitled Dragon Game')
clock = pygame.time.Clock()


test_surface = pygame.Surface((400, 300))
test_surface.fill('Red')

button_font = pygame.font.Font(None, 36)
list_font = pygame.font.Font(None, 18)

buttons = Buttton_List([], 115, 10, 200, 100, 10)
prog_buttons = Buttton_List([], 320, 10, 200, 100, 10)
res_gold = Resource('gold', 100)
res_potatoes = Resource('potatoes', 10, 0.01)
res_list1 = Res_List([res_gold, res_potatoes], 5, 5, 100, screen.get_height() - 10, 'grey', list_font, 0, 'black')
test_button0 = Button(blue_theme, (115, 10, 200, 100), button_font, parent= buttons, text= "hello", max_activations = 2)
test_button1 = Button(red_theme, (115, 120, 200, 100), button_font, parent= buttons, text = "hello again")
test_button2 = Button_Toggle(red_theme, (320, 10, 200, 100), button_font, 100, parent= prog_buttons, text = "progress", max_activations= 1)
event0 = Event(lambda : test_button1.activate())
event1 = Event(lambda : res_gold + 1, cost= [(res_potatoes, 1)])
event2null = Event(lambda : True)
event2p = Event(lambda : test_button2.prog(1), cost= [(res_gold, 0.01)])
test_button0.finish_event = event0
test_button1.finish_event = event1
test_button2.start_event = event2null
test_button2.progress_event = event2p
test_button2.finish_event = event2null
buttons + [test_button0]
prog_buttons + [test_button2]
def allbuttons():
    return buttons.list + prog_buttons.list

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for b in allbuttons():
                    if b.rect.collidepoint(pos):
                        b.clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for b in allbuttons():
                    b.clicked = False
                    if b.rect.collidepoint(pos):
                        b.click()
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                for b in allbuttons():
                    if b.rect.collidepoint(pos):
                        b.hovered = True
                    else:
                        b.hovered = False
        for r in res_list1.list:
            r.tick()
        for b in prog_buttons:
            if b.active:
                b.tick()
        screen.fill("dark grey")
        res_list1.draw(screen)
        for b in allbuttons():
            b.draw(screen)
        pygame.display.update()
        clock.tick(framerate)
main()