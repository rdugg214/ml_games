import pygame
import sys
import numpy as np

def run_menu():
    pygame.init()

    WIDTH = 800
    HEIGHT = 600
    FLOOR_HEIGHT = HEIGHT - 50
    background_colour = (0,0,0)

    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    menu_running = True

    while menu_running:
        screen.fill(background_colour)

        pygame.draw.rect(screen, (255, 255, 0), (400, 300, 20, 20))

        pygame.display.update()


if __name__ == "__main__":
    run_menu()
