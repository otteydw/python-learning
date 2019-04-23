#!/usr/bin/python3

import pygame

pygame.init()

width = 900
height = 700
screenDim = (width, height)

screen = pygame.display.set_mode(screenDim)

pygame.display.set_caption('My First Game')

grassImage = pygame.image.load(
    '/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/grass.png').convert()
grassImage = pygame.transform.scale(grassImage, screenDim)
screen.blit(grassImage, (0, 0))

rescale = 3

player = pygame.image.load(
    '/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/characterBody.png').convert_alpha()
playerWidth = player.get_rect().width
playerHeight = player.get_rect().height
player = pygame.transform.scale(
    player, (playerWidth*rescale, playerHeight*rescale))
player = pygame.transform.rotate(player, 90)
screen.blit(player, (0, 0))

foot = pygame.image.load(
    '/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/characterFoot.png').convert_alpha()
footWidth = foot.get_rect().width
footHeight = foot.get_rect().height
foot = pygame.transform.scale(
    foot, (footWidth*rescale, footHeight*rescale))
foot = pygame.transform.rotate(foot, 90)
screen.blit(foot, (0, 0))

rescaleBall = 2
ball = pygame.image.load(
    '/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/ball.png').convert_alpha()
ballWidth = ball.get_rect().width
ballHeight = ball.get_rect().height
player = pygame.transform.scale(
    ball, (ballWidth*rescaleBall, ballHeight*rescaleBall))
screen.blit(ball, (0, 0))

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
