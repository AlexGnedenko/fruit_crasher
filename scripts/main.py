import pygame
from pygame import *
from game_objects import *

# constants
DISPLAY_SIZE = (1280, 720)
FPS = 25


def main():
    # init PyGame, main drawing surface and FPS timer
    pygame.init()
    main_surface = pygame.display.set_mode(DISPLAY_SIZE, pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    # TO DO: load save
    balance = 1

    # init
    game_objects = GameObjects(balance)

    # main program loop
    while 1:
        # (1) get keyboard key pressed
        pressed_keys = pygame.key.get_pressed()

        # (2) update object states considering user_events
        game_objects.update_state(pressed_keys)

        # (3) draw all state
        game_objects.draw(main_surface)

        # FPS timer delay
        clock.tick(FPS)

        # exit
        for e in pygame.event.get():

            # выход, если системный выход
            if e.type == QUIT:
                pygame.display.quit()
                return
            # выход, если нажат ESCAPE
            elif pressed_keys[K_ESCAPE]:
                pygame.display.quit()
                return


if __name__ == "__main__":
    main()
