import sys
import pygame
from objects.shniffy import Shniffy
from preset import *
from entity import EntityHandler
from system import apply_vec

pygame.init()

canvas = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

dt = 0
entity_handler = EntityHandler(Shniffy(width /2, height /2 ))
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    entity_handler.update(events, dt)
    entity_handler.apply(apply_vec)
    canvas.blits(entity_handler.draw())

    dt = clock.tick(framerate)
    pygame.display.update()

sys.exit(0)