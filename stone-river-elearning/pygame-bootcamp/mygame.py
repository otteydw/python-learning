#!/usr/bin/python3

import pygame
import math

pygame.init()

class Game:
    def __init__(self, screen, screenDimensions):
        self.fps = 30
        self.screenDimensions = screenDimensions
        self.frame = pygame.time.Clock()
        self.screen = screen

    def updateFrame(self):
        self.frame.tick(self.fps)
        pygame.display.flip()

class Background(Game):
    def __init__(self, screen, screenDimensions):
        Game.__init__(self, screen, screenDimensions)
        self.goalLeft = None
        self.goalMiddle = None
        self.goalRight = None
        self.adjust = 12
        self.grassImages = None

    def loadGrass(self,name):
        self.grassImage = pygame.image.load(name).convert()
        self.grassImage = pygame.transform.scale(self.grassImage, self.screenDimensions)

    def cropSurface(newWidth, newHeight, cropWidth, cropHeight, image):
        newSurf = pygame.Surface((newWidth, newHeight), pygame.SRCALPHA, 32)     # 32-bit pixels
        newSurf.blit(image, (0, 0), (cropWidth, cropHeight, newWidth, newHeight))
        return newSurf

    def loadGoalLeft(self, name):
        self.goalLeft = pygame.image.load(name).convert_alpha()
        self.goalLeft = pygame.transform.scale(self.goalLeft, (250, 270))
        goalLeftWidth = self.goalLeft.get_rect().width
        goalLeftHeight = self.goalLeft.get_rect().height
        self.goalLeft = cropSurface(goalLeftWidth/2+self.adjust, goalLeftHeight/2 + self.adjust, goalLeftWidth/2-self.adjust, goalLeftHeight/2-self.adjust, self.goalLeft)

    def loadGoalMiddle(self, name):
        self.goalMiddle = pygame.image.load(name).convert_alpha()
        self.goalMiddle = pygame.transform.scale(self.goalMiddle, (250, 270))
        goalMiddleWidth = self.goalMiddle.get_rect().width
        goalMiddleHeight = self.goalMiddle.get_rect().height
        self.goalMiddle = cropSurface(goalMiddleWidth, goalMiddleHeight/2+self.adjust, 0, goalMiddleHeight/2-self.adjust, self.goalMiddle)

    def loadGoalRight(self, name):
        self.goalRight = pygame.image.load(name).convert_alpha()
        self.goalRight = pygame.transform.scale(self.goalRight, (250, 270))
        goalRightWidth = self.goalRight.get_rect().width
        goalRightHeight = self.goalRight.get_rect().height
        self.goalRight = cropSurface(goalRightWidth/2+self.adjust, goalRightHeight/2+self.adjust, 0, goalRightHeight/2-self.adjust, self.goalRight)

    def setStart(self):
        self.goalStart = (self.screenDimensions[0] - self.goalLeft.get_rect().width - self.goalMiddle.get_rect().width - self.goalRight.get_rect().width)/2

    def blitBackground(self):
        self.screen.blit(self.grassImage, (0, 0))
        self.screen.blit(self.goalLeft, (self.goalStart, 0,))
        self.screen.blit(self.goalMiddle, (self.goalStart + self.goalLeft.get_rect().width, 0,))
        self.screen.blit(self.goalRight, (self.goalStart + self.goalLeft.get_rect().width + self.goalMiddle.get_rect().width, 0,))

class Ball(Game):
    def __init__(self, screen, screenDimensions):
        Game.__init__(self, screen, screenDimensions)
        self.ballX = self.screenDimensions[0]/2
        self.ballY = 450
        self.ball = None

    def loadBall(self, name, rescaleBall):
        self.ball = pygame.image.load(name).convert_alpha()
        ballWidth = self.ball.get_rect().width
        ballHeight = self.ball.get_rect().height
        self.ball = pygame.transform.scale(self.ball, (ballWidth*rescaleBall, ballHeight*rescaleBall))

    def blitBall(self):
        self.screen.blit(self.ball, (self.ballX - self.ball.get_rect().width / 2, self.ballY - self.ball.get_rect().height/2))

    def setKickDirection(self, playerX, playerY):
        xMove=(playerX - self.ballX)/10    # Make small steps toward the ball
        yMove=(playerY - self.ballY)/10
        normMove=1/math.sqrt(xMove**2 + yMove**2)
        self.ballXDirection = xMove * normMove
        self.ballYDirection = yMove * normMove

    def kickBall(self,speed):
        self.ballX -= speed*self.ballXDirection
        self.ballY -= speed*self.ballYDirection

class Player(Game):
    def __init__(self, screen, screenDimensions):
        Game.__init__(self, screen, screenDimensions)
        self.player = None
        self.playerStart=self.player
        self.foot = None
        self.footStart=self.foot

        self.playerX=screenDimensions[0]/2
        self.playerY=530
        self.playerXOriginal=self.playerX
        self.playerYOriginal=self.playerY

        self.footX = None
        self.footY = None

        self.currentRotation = 0
        self.radius = 80
        self.deltaTheta = int(90/(self.radius/5))

    def loadPlayer(self, name, rescale):
        self.player = pygame.image.load(name).convert_alpha()
        playerWidth = self.player.get_rect().width
        playerHeight = self.player.get_rect().height
        self.player = pygame.transform.scale(self.player, (playerWidth*rescale, playerHeight*rescale))
        self.player = pygame.transform.rotate(self.player, 90)
        self.playerStart = self.player

    def loadFoot(self, name, rescale):
        self.foot = pygame.image.load(name).convert_alpha()
        footWidth = self.foot.get_rect().width
        footHeight = self.foot.get_rect().height
        self.foot=pygame.transform.scale(self.foot, (footWidth*rescale, footHeight*rescale))
        self.foot = pygame.transform.rotate(self.foot, 90)
        self.footStart=self.foot

    def rotatePlayer(self, angle):
        self.player = pygame.transform.rotate(self.playerStart, angle)
        # self.player = pygame.transform.rotate(self.player, angle)

    def rotateFoot(self, angle):
        self.foot = pygame.transform.rotate(self.footStart, angle)
        # self.foot = pygame.transform.rotate(self.foot, angle)

    def movePlayer(self, direction):
        if direction == 'Left':
            self.deltaTheta *= -1
        finalRot = (self.currentRotation+self.deltaTheta)*math.pi/180    # Final position in radians

        Hypotenuse = (self.radius * math.sin(finalRot)/(math.sin((math.pi - finalRot)/2)))
        changeX = Hypotenuse * math.cos(math.pi/2 - (math.pi-finalRot)/2)
        changeY = Hypotenuse * math.sin(math.pi/2 - (math.pi-finalRot)/2)

        self.currentRotation = self.currentRotation + self.deltaTheta
        self.player = pygame.transform.rotate(self.playerStart, self.currentRotation+self.deltaTheta)
        self.playerX = self.playerXOriginal + changeX
        self.playerY = self.playerYOriginal - changeY

        if direction == 'Left': # revert
            self.deltaTheta *= -1

    def blitPlayer(self):
        self.screen.blit(self.player, (self.playerX - self.player.get_rect().width / 2, self.playerY - self.player.get_rect().height/2))

    def blitFoot(self):
        self.screen.blit(self.foot, (self.footX - self.foot.get_rect().width/2, self.footY - self.foot.get_rect().height/2))

    def playerShoot(self, ballX, ballY):
        xMove = (self.playerX - ballX)/10    # Make small steps toward the ball
        yMove = (self.playerY - ballY)/10
        self.playerX -= xMove
        self.playerY -= yMove

    def positionFoot(self, ballX, ballY):
        xMove = (self.playerX - ballX)/10    # Make small steps toward the ball
        yMove = (self.playerY - ballY)/10
        normMove = 1/math.sqrt(xMove**2 + yMove**2)
        distanceToShoulder = 20
        shoulderAngle = self.currentRotation*math.pi/180
        self.footX = (self.playerX + distanceToShoulder * math.cos(shoulderAngle) - 20*xMove*normMove)
        self.footY=(self.playerY - distanceToShoulder * math.sin(shoulderAngle) - 20*yMove*normMove)
        self.foot = pygame.transform.rotate(self.footStart,self.currentRotation)

def cropSurface(newWidth, newHeight, cropWidth, cropHeight, image):
    newSurf = pygame.Surface((newWidth, newHeight), pygame.SRCALPHA, 32)     # 32-bit pixels
    newSurf.blit(image, (0, 0), (cropWidth, cropHeight, newWidth, newHeight))
    return newSurf

# def movePlayer(direction,radius,absRot):
#     yChange = 5
#     deltaTheta = int(90/(radius/yChange))
#     if direction == 'Left':
#         deltaTheta *= -1
#     finalRot = (absRot + deltaTheta)*math.pi/180    # Final position in radians

#     Hypotenuse = (radius * math.sin(finalRot)/(math.sin((math.pi - finalRot)/2)))
#     newX = Hypotenuse * math.cos(math.pi/2 - (math.pi-finalRot)/2)
#     newY = Hypotenuse * math.sin(math.pi/2 - (math.pi-finalRot)/2)
#     return newX, newY, absRot + deltaTheta

def updateFrameImages(showFoot = False):
    global background, newPlayer, newBall
    background.blitBackground()

    if showFoot:
        newPlayer.blitFoot()

    newPlayer.blitPlayer()
    newBall.blitBall()

width = 900
height = 700
screenDim = (width, height)

screen = pygame.display.set_mode(screenDim)

pygame.display.set_caption('My First Game')

game = Game(screen, screenDim)
newPlayer = Player(screen, screenDim)
newBall = Ball(screen, screenDim)
background = Background(screen, screenDim)

background.loadGrass('/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/grass.png')

rescale = 3
newPlayer.loadPlayer('/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/characterBody.png', rescale)
newPlayer.loadFoot('/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/characterFoot.png', rescale)

rescaleBall = 2
newBall.loadBall('/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/ball.png', rescaleBall)

background.loadGoalLeft('/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/goalLeft.png')

goalHeight = background.goalLeft.get_rect().height

background.loadGoalMiddle('/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/goalMiddle.png')

background.loadGoalRight('/home/dottey/git/python-learning/stone-river-elearning/pygame-bootcamp/images/goalRight.png')

background.setStart()

background.blitBackground()

newPlayer.blitPlayer()

newBall.blitBall()

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
        if newPlayer.currentRotation > -90:
            newPlayer.movePlayer('Left')
    elif pressedKeys[pygame.K_RIGHT]:
        print("RIGHT KEY")
        if newPlayer.currentRotation < 90:
            newPlayer.movePlayer('Right')
    elif pressedKeys[pygame.K_SPACE]:
        # I think this catches multiple space presses on a single press.  It causes the player to sometimes move after it reaches the ball.
        print("SPACE KEY")
        for i in range(3):
            newPlayer.playerShoot(newBall.ballX, newBall.ballY)
            updateFrameImages()
            game.updateFrame()
        newPlayer.positionFoot(newBall.ballX, newBall.ballY)
        updateFrameImages(True)
        game.updateFrame()

        newBall.setKickDirection(newPlayer.playerX, newPlayer.playerY)
        speed = 20
        while newBall.ballY >= goalHeight:
            newBall.kickBall(speed)
            updateFrameImages()
            game.updateFrame()

    updateFrameImages()
    game.updateFrame()
pygame.quit()
