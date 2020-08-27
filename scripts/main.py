import pygame
from pygame import *
from game_objects import *
import json

# constants
DISPLAY_SIZE = (1280, 720)
FPS = 25


def main():
    # init PyGame, main drawing surface and FPS timer
    pygame.init()
    main_surface = pygame.display.set_mode(DISPLAY_SIZE, pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    # load save
    SKILLS_file = "../settings/SAVE.json"
    with open(SKILLS_file) as f:
        skills = json.load(f)
    balance = skills["balance"]

    # init and play fon music
    game_objects = GameObjects(balance)
    game_objects.play_music()

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
