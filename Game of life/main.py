import pygame
import time
import random
import numpy as np
import os
import grid


width, height = 1080, 720
size = (width, height)

pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

black = (0, 0, 0)
white = (255, 255, 255)

scaler = 10
offset = 1

Grid = grid.Grid(width, height, scaler, offset)
Grid.random2d_array()


run = True
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Grid.Conway(off_color=white, on_color=black, surface=screen)
    pygame.display.update()

pygame.quit()
