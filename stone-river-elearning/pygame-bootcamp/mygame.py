#!/usr/bin/python3

import pygame

pygame.init()


def cropSurface(newWidth, newHeight, cropWidth, cropHeight, image):
    newSurf = pygame.Surface((newWidth, newHeight),
                             pygame.SRCALPHA, 32)     # 32-bit pixels
    newSurf.blit(image, (0, 0), (cropWidth, cropHeight, newWidth, newHeight))
    return newSurf


width = 900
height = 700
screenDim = (width, height)

screen = pygame.display.set_mode(screenDim)

pygame.display.set_caption('My First Game')

grassImage = pygame.image.load(
    '/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/grass.png').convert()
grassImage = pygame.transform.scale(grassImage, screenDim)

rescale = 3
player = pygame.image.load(
    '/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/characterBody.png').convert_alpha()
playerWidth = player.get_rect().width
playerHeight = player.get_rect().height
player = pygame.transform.scale(
    player, (playerWidth*rescale, playerHeight*rescale))
player = pygame.transform.rotate(player, 90)

foot = pygame.image.load(
    '/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/characterFoot.png').convert_alpha()
footWidth = foot.get_rect().width
footHeight = foot.get_rect().height
foot = pygame.transform.scale(
    foot, (footWidth*rescale, footHeight*rescale))
foot = pygame.transform.rotate(foot, 90)

rescaleBall = 2
ball = pygame.image.load(
    '/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/ball.png').convert_alpha()
ballWidth = ball.get_rect().width
ballHeight = ball.get_rect().height
ball = pygame.transform.scale(
    ball, (ballWidth*rescaleBall, ballHeight*rescaleBall))

goalLeft = pygame.image.load(
    '/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/goalLeft.png').convert_alpha()
goalLeft = pygame.transform.scale(goalLeft, (250, 270))
goalLeftWidth = goalLeft.get_rect().width
goalLeftHeight = goalLeft.get_rect().height
adjust = 12
goalLeft = cropSurface(goalLeftWidth/2+adjust, goalLeftHeight/2 +
                       adjust, goalLeftWidth/2-adjust, goalLeftHeight/2-adjust, goalLeft)

goalMiddle = pygame.image.load(
    '/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/goalMiddle.png').convert_alpha()
goalMiddle = pygame.transform.scale(goalMiddle, (250, 270))
goalMiddleWidth = goalMiddle.get_rect().width
goalMiddleHeight = goalMiddle.get_rect().height
goalMiddle = cropSurface(
    goalMiddleWidth, goalMiddleHeight/2+adjust, 0, goalMiddleHeight/2-adjust, goalMiddle)

goalRight = pygame.image.load(
    '/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/goalRight.png').convert_alpha()
goalRight = pygame.transform.scale(goalRight, (250, 270))
goalRightWidth = goalRight.get_rect().width
goalRightHeight = goalRight.get_rect().height
goalRight = cropSurface(
    goalRightWidth/2+adjust, goalRightHeight/2+adjust, 0, goalRightHeight/2-adjust, goalRight)

screen.blit(grassImage, (0, 0))

goalStart = (width - goalLeft.get_rect().width -
             goalMiddle.get_rect().width - goalRight.get_rect().width)/2
screen.blit(goalLeft, (goalStart, 0,))
screen.blit(goalMiddle, (goalStart + goalLeft.get_rect().width, 0,))
screen.blit(goalRight, (goalStart + goalLeft.get_rect().width +
                        goalMiddle.get_rect().width, 0,))

playerX = width/2
playerY = 530
screen.blit(player, (playerX - player.get_rect().width /
                     2, playerY - player.get_rect().height/2))
# screen.blit(foot, (0, 0))

ballX = width/2
ballY = 450
screen.blit(ball, (ballX - ball.get_rect().width /
                   2, ballY - ball.get_rect().height/2))

frame = pygame.time.Clock()
finished = False
while not finished:

    # Process all the events
    for event in pygame.event.get():
        # Do the things
        print(event)    # Debug
        if event.type == pygame.QUIT:
            finished = True

    pressedKeys = pygame.key.get_pressed()

    if pressedKeys[pygame.K_LEFT]:
        print("LEFT KEY")
    elif pressedKeys[pygame.K_RIGHT]:
        print("RIGHT KEY")
    elif pressedKeys[pygame.K_SPACE]:
        print("SPACE KEY")

    pygame.display.flip()   # Update the display
    frame.tick(30)  # FPS
pygame.quit()
