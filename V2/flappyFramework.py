import pygame
from pygame.locals import *  # noqa
import sys
import random


global QUIT, MOUSECLICK
QUIT = pygame.QUIT
MOUSECLICK = pygame.MOUSEBUTTONDOWN

'''
A flappy bird framework developed to help teach young students the basic of programming
'''

class FlappyBird:
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 708))
        self.score = 0
        self.offset = random.randint(-110, 110)

        pygame.init()

        self.sounds = {}
        self.sounds['die'] = pygame.mixer.Sound('assets/die.wav')
        self.sounds['hit'] = pygame.mixer.Sound('assets/hit.wav')
        self.sounds['point'] = pygame.mixer.Sound('assets/point.wav')
        self.sounds['swoosh'] = pygame.mixer.Sound('assets/swoosh.wav')
        self.sounds['wing'] = pygame.mixer.Sound('assets/wing.wav')

    def loadBackground(self):
        self.background = pygame.image.load("assets/background.png").convert()

    def nameScreen(self, title):
        pygame.display.set_caption(title)

    def playSound(self, soundName):
        self.sounds[soundName].play()

    def loadBird(self):
        self.bird = pygame.Rect(65,50,50,50)
        self.jump = 0
        self.jumpSpeed = 0
        self.gravity = 5
        self.dead = False
        self.sprite = 0
        self.birdY = 350
        self.birdSprites = random.choice([[pygame.image.load("assets/1.png").convert_alpha(),
    						pygame.image.load("assets/2.png").convert_alpha(),
    						pygame.image.load("assets/dead.png")],
                            [pygame.image.load("assets/bluebird-downflap.png").convert_alpha(),
                            pygame.image.load("assets/bluebird-upflap.png").convert_alpha(),
                            pygame.image.load("assets/dead.png")],
                            [pygame.image.load("assets/redbird-downflap.png").convert_alpha(),
                            pygame.image.load("assets/redbird-upflap.png").convert_alpha(),
                            pygame.image.load("assets/dead.png")]])

    def loadWalls(self, gap):
   		self.wallUp = pygame.image.load("assets/bottom.png").convert_alpha()
   		self.wallDown = pygame.image.load("assets/top.png").convert_alpha()
   		self.gap = gap
   		self.wallx = 400

    def updateWalls(self):
        self.wallx -= 2
        if self.wallx < -80:
            self.wallx = 400
            self.offset = random.randint(-110, 110)

    def birdUpdate(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
            self.jump -= 1
        else:
            self.birdY += self.gravity
            self.gravity += 0.2
        self.bird[1] = self.birdY

    def checkHitTopPipe(self):
        upRect = pygame.Rect(self.wallx, 360 + self.gap - self.offset + 10, self.wallUp.get_width() - 10, self.wallUp.get_height())

        if upRect.colliderect(self.bird):
            return True

    def checkHitBottomPipe(self):
        downRect = pygame.Rect(self.wallx, 0 - self.gap - self.offset - 10, self.wallDown.get_width() - 10, self.wallDown.get_height())

        if downRect.colliderect(self.bird):
            return True            

    def resetGame(self):
        self.bird[1] = 50
        self.birdY = 50
        self.dead = False
        self.score = 0
        self.wallx = 400
        self.offset = random.randint(-110, 110)
        self.gravity = 5

    def birdNotDead(self):
    	return not self.dead

    def birdDead(self):
    	return self.dead

    def getClock(self):
    	return pygame.time.Clock()

    def getEvent(self):
    	return pygame.event.get()

    def exit():
    	sys.exit()

    def birdJump(self):
    	self.jump = 17
    	self.gravity = 5
    	self.jumpSpeed = 10

    def updateScreen(self):
    	self.screen.fill((255,255,255))
    	self.screen.blit(self.background, (0,0))
    	self.screen.blit(self.wallUp, (self.wallx, 360+self.gap-self.offset))
    	self.screen.blit(self.wallDown, (self.wallx, 0-self.gap-self.offset))
    	self.screen.blit(font.render(str(self.score), -1, (255,255,255)), (200,50))

    def updateBirdImage(self):
    	if self.dead:
    		self.sprite = 2
    	elif self.jump:
    		self.sprite = 1

    	self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))

    	if not self.dead:
    		self.sprite = 0


#The following is a suggested solution
#TODO: Add flexibility/more coding for the students

if __name__ == "__main__":

    game = FlappyBird()

    title = "FLAPPY"
    game.nameScreen(title)

    game.loadBackground()
    game.loadBird()

    gap = 200

    game.loadWalls(gap)
    
    clock = game.getClock()
    pygame.font.init()

    fontName = "Arial"
    fontSize = 50

    font = pygame.font.SysFont(fontName, fontSize)
    gameSpeed = 60

    while True:
    	clock.tick(gameSpeed)

    	buttonsPressed = game.getEvent()

    	for button in buttonsPressed:

    		if button.type == QUIT:
    			game.exit()

    		if button.type == MOUSECLICK and game.birdNotDead():
    			game.playSound("wing")
    			game.birdJump()


    	game.updateScreen()
    	game.updateBirdImage()

    	#If we want score to increment by 1 let if condition be < -80 (could be hard to explain, 0 seems like an easy number)
    	if game.wallx <= -80:
    		game.score = game.score + 1

    	game.updateWalls()
    	game.birdUpdate()

    	if game.checkHitBottomPipe() == True:
    		game.playSound("die")
    		game.dead = True

    	if game.checkHitTopPipe() == True:
    		game.dead = True

    	#If bird out of bounds
    	if not 0 < game.bird[1] < 720:
    		game.resetGame()

    	pygame.display.update()





'''
if __name__ == "__main__":

    game = FlappyBird()

    title = _____ #What do you want the screent o be called?
    game.nameScreen(title)

    game.loadBackground()
    game.loadBird()

    gap = ______ #How big do you want the space to be between the pipes?
    
    game.loadWalls(gap)
    
    
    clock = game.getClock()
    pygame.font.init()

    fontName = ____ #Try some of your favorite fonts like "Arial" (string)
    fontSize = ____ #How big do you want the score to be (int)

    font = pygame.font.SysFont(fontName, fontSize)

    gameSpeed = _____ #Change this up, what do you think it does? What type does it need to be?

    while ______: #We want the game to keep running, so what should we put in here?

        clock.tick(gameSpeed)

        buttonsPressed = game.getEvent()

        for ______ in ________: #Answer: button (or whatever variable name you want) in buttonsPressed

            if button.type == _______: #Use the global QUIT
                ________ #Lets close the window since the user clicked X, game.exit()

            if button.type == ________ and _____________: #Use the global MOUSECLICK, the second blank is to check if the bird is dead game.birdNotDead()
            	game.playSound(_______) #What sound do you want to play? (give them a list of the sounds available)
                _________ #Since the bird isnt dead and the user clicked, we want it to jump so game.birdJump()

        game.updateScreen()
        game.updateBirdImage()

        if game.wallx < -80:
            game.score = game.score + _____ #How much do you want the score to increase by?

        game.updateWalls()
        game.birdUpdate()

        if game.checkHitBottomPipe() == ______: #What goes in here? (True)
        	game.playSound(_______) #What sound do you want to play? (give them a list of the sounds available)
            game.dead = True

        if game.checkHitTopPipe() == ____: #How about here? (True)
            game.dead = True

        #If bird out of bounds
        if not 0 < game.bird[1] < 720:
            ___________ #If the bird is out of bounds we want to call game.resetGame()

        pygame.display.update()
'''