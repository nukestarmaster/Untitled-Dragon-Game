import pygame
from button import Button
from sys import exit

width = 800
height = 600
framerate = 60
test_button = Button('red', 'blue', 50, 100, 100, 200, button_event= print)
test_button2 = Button('blue', 'red', 200, 300, 100, 200, button_event= lambda str: print(f"{str} 2") )
buttons = [test_button, test_button2]

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Untitled Dragon Game')
clock = pygame.time.Clock()
test_surface = pygame.Surface((400, 300))
test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for b in buttons:
                if b.rect.collidepoint(pos):
                    b.button_event('clicked')   
    screen.fill("dark grey")
    for b in buttons:
        b.draw(screen)
    pygame.display.update()
    clock.tick(framerate)