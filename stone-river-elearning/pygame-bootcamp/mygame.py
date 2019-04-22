#!/usr/bin/python3

import pygame

pygame.init()

width = 900
height = 700
screenDim = (width, height)

screen = pygame.display.set_mode(screenDim)

finished = False
while not finished:

    # Process all the events
    for event in pygame.event.get():
        # Do the things
        print(event)    # Debug
        if event.type == pygame.QUIT:
            finished = True

    pygame.display.flip()   # Update the display

pygame.quit()
