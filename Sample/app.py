import pygame
from pygame.locals import *
import sys
import os

class App:
    pygame.init()

# Set up the game window
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Hello Pygame")

# Game loop
    running = True
    while running:
        for event in pygame.event.get():
           x = x + 1
            if x = 10:
                pygame.quit()


# Quit Pygame
    
