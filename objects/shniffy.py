from typing import List
import pygame
from pygame.event import Event
from pygame.surface import Surface as Surface
from entity import Entity

class Shniffy(Entity):
    def __init__(self, x : int, y : int) -> None:
        self.x = x
        self.y = y
        self.left = pygame.image.load("sprites/shniffy-v1.png").convert()
        self.right = pygame.transform.flip(self.left, 1,0).convert()
        self.sprite = self.left

    def draw(self) -> Surface:
        return self.sprite
    
    def update(self, events: List[Event], dt_s: float):
        key_press_events : List[Event] = list(filter(lambda e: e.type == pygame.KEYDOWN, events))
        if key_press_events:
            key_press = key_press_events.pop()
        else:
            return
        if self.vx <= 0:
            self.sprite = self.right
        else:
            self.sprite = self.left
        if key_press.key == pygame.K_LEFT:
            self.vx -= 1
        if key_press.key == pygame.K_RIGHT:
            self.vx += 1
        