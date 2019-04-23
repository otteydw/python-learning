#!/usr/bin/python3

import pygame

pygame.init()


def cropSurface(newWidth, newHeight, cropWidth, cropHeight, image):
    newSurf = pygame.Surface((newWidth, newHeight), pygame.SRCALPHA, 32)     # 32-bit pixels
    newSurf.blit(image,(0,0), (cropWidth, cropHeight, newWidth, newHeight))
    return newSurf

width = 900
height = 700
screenDim = (width, height)

screen = pygame.display.set_mode(screenDim)

pygame.display.set_caption('My First Game')

grassImage = pygame.image.load('/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/grass.png').convert()
grassImage = pygame.transform.scale(grassImage, screenDim)
screen.blit(grassImage, (0, 0))

rescale = 3

player = pygame.image.load('/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/characterBody.png').convert_alpha()
playerWidth = player.get_rect().width
playerHeight = player.get_rect().height
player = pygame.transform.scale(
    player, (playerWidth*rescale, playerHeight*rescale))
player = pygame.transform.rotate(player, 90)
# screen.blit(player, (0, 0))

foot = pygame.image.load('/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/characterFoot.png').convert_alpha()
footWidth = foot.get_rect().width
footHeight = foot.get_rect().height
foot = pygame.transform.scale(
    foot, (footWidth*rescale, footHeight*rescale))
foot = pygame.transform.rotate(foot, 90)
# screen.blit(foot, (0, 0))

rescaleBall = 2
ball = pygame.image.load('/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/ball.png').convert_alpha()
ballWidth = ball.get_rect().width
ballHeight = ball.get_rect().height
player = pygame.transform.scale(
    ball, (ballWidth*rescaleBall, ballHeight*rescaleBall))
# screen.blit(ball, (0, 0))

# goalRescale = 2
goalLeft = pygame.image.load('/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/goalLeft.png').convert_alpha()
goalLeft = pygame.transform.scale(goalLeft,(250,270))
goalLeftWidth = goalLeft.get_rect().width
goalLeftHeight = goalLeft.get_rect().height
# goalLeft = pygame.transform.scale(
#     goalLeft, (goalLeftWidth*goalRescale, goalLeftHeight*goalRescale))
adjust=12
goalLeft = cropSurface(goalLeftWidth/2+adjust, goalLeftHeight/2+adjust, goalLeftWidth/2-adjust, goalLeftHeight/2-adjust, goalLeft)
screen.blit(goalLeft, (0, 0,))

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
