#!/usr/bin/python3

import pygame

pygame.init()

width = 900
height = 700
screenDim = (width, height)

screen = pygame.display.set_mode(screenDim)

pygame.display.set_caption('My First Game')

grassImage = pygame.image.load(
    '/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/grass.png')
grassImage = pygame.transform.scale(grassImage, screenDim)
screen.blit(grassImage, (0, 0))

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
