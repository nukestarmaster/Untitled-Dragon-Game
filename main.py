import pygame
from graphics.button import Button
from graphics.colour_themes import Button_Theme
from graphics.res_list import Res_List
from logic.resource import Resource
from sys import exit

width = 800
height = 600
framerate = 60
red_theme = Button_Theme('red', 'grey', (131, 0, 0), 'black', 'black', 'dark grey')
blue_theme = Button_Theme('blue', 'grey', (0, 0, 131), 'black', 'black', 'dark grey')

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Untitled Dragon Game')
clock = pygame.time.Clock()


test_surface = pygame.Surface((400, 300))
test_surface.fill('Red')

button_font = pygame.font.Font(None, 36)
list_font = pygame.font.Font(None, 18)

res_gold = Resource('gold', 100)
res_potatoes = Resource('potatoes', 10)
res_list1 = Res_List([res_gold, res_potatoes], 5, 5, 100, height - 5, 'grey', list_font, 0, 'black')

test_button2 = Button(red_theme, 115, 120, 100, 200, button_font, text = "hello again", button_event= lambda : res_gold + 1)
test_button = Button(blue_theme, 115, 10, 100, 200, button_font, True, text= "hello", button_event= test_button2.activate)
buttons = [test_button, test_button2]

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for b in buttons:
                    if b.active and b.rect.collidepoint(pos):
                        b.clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for b in buttons:
                    b.clicked = False
                    if b.active and b.rect.collidepoint(pos):
                        b.button_event()
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                for b in buttons:
                    if b.active and b.rect.collidepoint(pos):
                        b.hovered = True
                    else:
                        b.hovered = False
        screen.fill("dark grey")
        res_list1.draw(screen)
        for b in buttons:
            b.draw(screen)
        pygame.display.update()
        clock.tick(framerate)

main()