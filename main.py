# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    pygame.init()
    setScreen()

#function to set the game screen
def setScreen():
    #set display dimensions and create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #set the window title
    pygame.display.set_caption("Asteroids")
    
    #setting fps
    clock = pygame.time.Clock()
    
    dt = 0

    #groups to manage game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #adding the groups to the player class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers =(shots, updatable, drawable)

    asterfield1 = AsteroidField()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player1 = Player(x,y)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #move the player around
        for i in updatable:
            i.update(dt)

        for i in asteroids:
            if i.checkCollision(player1) == True:
                print("Game Over!")
                running = False
            for j in shots:
                if i.checkCollision(j) == True:
                    j.kill()
                    i.split()


        #fill the screen with black color
        screen.fill((0,0,0))

        #re-render the player on the screen each frame
        for i in drawable:
            i.draw(screen)

        #update the display
        pygame.display.flip()

        #call the tick method to pause for define time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
