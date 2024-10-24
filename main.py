# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import CircleShape

class Player (CircleShape):
    def __init__(self,x,y):
        super().__init__(PLAYER_RADIUS,x,y)
        self.rotation = 0


def main ():
    pygame.init ()
    clock = pygame.time.Clock ()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Ensure x and y are defined as appropriate


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    print("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen hbootdev run 268bb0d0-3e63-4218-aacc-cba3247a1af5 -seight: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()