from typing import Type
from component import Collision
from entity import Entity


def apply_vec(entity: Entity):
    entity.x += entity.vx
    entity.y += entity.vy