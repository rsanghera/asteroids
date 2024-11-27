# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *

def main():
    print("Starting asteroids!")
    pygame.init()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player1 = Player(x,y)
    setScreen(player1)

#function to set the game screen
def setScreen(player):
    #setting fps
    clock = pygame.time.Clock()
    dt = 0

    #set display dimensions and create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #set the window title
    pygame.display.set_caption("Asteroids")

    #fill the screen with black color
    screen.fill((0,0,0))

    #re-render the player on the screen each frame
    player.draw(screen)

    #update the display
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():

            #call the tick method to pause for define time
            clock.tick(60)
            dt = clock.tick() / 1000  
            if event.type == pygame.QUIT:
                return
    
    #quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()
