# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

#function to set the game screen
def setScreen():
    #setting fps
    clock = pygame.time.Clock()
    dt = 0

    #set display dimensions and create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #set the window title
    pygame.display.set_caption("Asteroids")

    #fill the screen with black color
    screen.fill((0,0,0))

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
    pygame.init()
    main()
    setScreen()
