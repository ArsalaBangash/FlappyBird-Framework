
from flappyFramework import *

'''This is a Integer Varible'''
## This variable controls speed of the game - you can  change its value to make the game go faster or slower
game_speed = 3
'''This is a String Varible'''
## This variable controls the background of the game - you can  change its value choose between the night and day background
game_background = "day"
'''This is a String Varible'''
## This variable controls the color of the bird - you can  change its value choose between the different color of the bird
game_color = "red"

'''This is a String Varible'''
## This variable controls the name of the game - you can  change its value choose the name of the game
game_name = "Flappy Bird"




'''Conditional Statements'''
## write a conditional statement that allows the user to escape the game use from API following functions - escapePressed, closeGame
def check_escape(buttonsPressed):
    ##if escapePressed(buttonsPressed):
            ##closeGame()
## write a conditional statement that allows the user to make the bird fly when mouse is clicked API following functions - mouseClick, birdNotDead, birdJump
## note - remeber to check if the bird is dead in the if statement
def click_to_move(game, buttonsPressed):
    ##if mouseClick(buttonsPressed) and game.birdNotDead():
    	##game.birdJump()
## write a conditional statement that checks weather the bird passed the wall and increament the game.score variable API following functions - wallPassed, birdNotDead
## note - remeber to check if the bird is dead in the if statement
def score_update(game):
    ##if game.wallPassed() and game.birdNotDead():
    	##game.score = game.score + 1 #This can be a fcn but we think its good for them to learn

## write a conditional statement that checks weather the bird hit one of the pipes  API following functions - checkHitBottomPipe, checkHitBottomPipe
## note - two condition in the conditional statment
## advance use or to combine two conditional statments
def Pipe_hit(game):
    ##if game.checkHitBottomPipe() == True or game.checkHitTopPipe() == True:
       ## game.over = True

    
