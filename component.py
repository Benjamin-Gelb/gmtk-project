class Position:
    x: int = 0
    y: int = 0

class Velocity:
    vx: float = 0
    vy: float = 0

class Collision:
    width: int
    height: int


# class Sprite:
#     images: List[pygame.Surface]
#     def __init__(self, images: List[pygame.Surface], idx = 0) -> None:
#         self.images = images
#         self.idx = idx
#     def __getitem__(self, idx: int):
#         self.images[idx]
#     def __sizeof__(self) -> int:
#         return len(self.images)
#     def tick(self, dt_s: float):
#         pass
#     def current_frame(self):
#         return self.images[self.idx]


# class Animation:
#     def __init__(self, sprite: Sprite, fps: int) -> None:
#         self.sprite = sprite
#         self.frame_time = 1 / fps
#         self.frame_idx = 0
#         self.total_frames = len(sprite.images)
#         self.elapsed = 0.0

#     def tick(self, dt_s: float):
#         self.elapsed += dt_s
#         if self.elapsed >= self.frame_time:
#             self.frame_idx += 1
#             self.elapsed = 0.0

#         if self.frame_idx >= self.total_frames:
#             self.frame_idx = 0

#     def current_frame(self):
#         return self.sprite[self.frame_idx]