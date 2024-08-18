from abc import ABC, abstractmethod
import pygame
from typing import Any, Callable, List, Tuple
from component import Collision, Position, Velocity

class Entity(Position, Velocity, ABC):
    @abstractmethod
    def draw(self) -> pygame.Surface:
        pass
    @abstractmethod
    def update(self, events: List[pygame.event.Event], dt_s: float):
        pass

class EntityHandler:
    def __init__(self, *entities: Entity) -> None:
        self.entities: List[Entity] = [*entities]

    def add(self, entity: Entity):
        self.entities.append(entity)

    def update(self, events: List[pygame.event.Event], dt_s: float):
        for entity in self.entities:
            entity.update(events, dt_s)

    def draw(self) -> Tuple[pygame.Surface, Tuple[int, int]]:
        return [(entity.draw(), (entity.x, entity.y)) for entity in self.entities]

    def apply(self, apply_func: Callable[[Entity], Any]):
        for entity in self.entities:
            apply_func(entity)
