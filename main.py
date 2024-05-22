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

res_gold = Resource('Gold', 100)
res_potatoes = Resource('Stone', 10, 0.01)
res_list1 = Res_List([res_gold, res_potatoes], 5, 5, 100, screen.get_height() - 10, 'grey', list_font, 0, 'black')

res_action = Resource('Action', 1, 0.01)
res_list2 = Res_List([res_action], screen.get_height() - 5, 5, 100, screen.get_height() - 10, 'grey', list_font, 0, 'black')

buttons = Buttton_List([], 115, 10, 200, 100, 10)
prog_buttons = Buttton_List([], 320, 10, 200, 100, 10)

button_hatch = Button(blue_theme, (115, 10, 200, 100), button_font, parent= buttons, text= "Hatch", max_activations = 5)
test_button1 = Button(red_theme, (115, 120, 200, 100), button_font, parent= buttons, text = "hello again")
test_button2 = Button_Toggle(red_theme, (320, 10, 200, 100), button_font, 100, progress_tick= 1, parent= prog_buttons, text = "progress", max_activations= 1)

event_hatch0 = Event(cost= [(res_action, 0.99)])
event_hatch = Event(lambda : test_button1.activate())
event1 = Event(lambda : res_gold + 1, cost= [(res_potatoes, 1)])
event2p = Event(lambda : True, cost= [(res_gold, 0.1)])

button_hatch.finish_event = event_hatch0
button_hatch.activation_dict = {5: event_hatch}
test_button1.finish_event = event1
test_button2.progress_event = event2p

buttons + [button_hatch]
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
                        break
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                for b in allbuttons():
                    if b.rect.collidepoint(pos):
                        b.hovered = True
                    else:
                        b.hovered = False
        for r in res_list1.list:
            r.tick()
        for r in res_list2.list:
            r.tick()
        for b in prog_buttons:
            if b.active:
                b.tick()
        screen.fill("dark grey")
        res_list1.draw(screen)
        res_list2.draw(screen)
        for b in allbuttons():
            b.draw(screen)
        pygame.display.update()
        clock.tick(framerate)
main()