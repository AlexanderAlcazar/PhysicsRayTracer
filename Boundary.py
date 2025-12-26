import math
import pygame

WHITE = (255, 255, 255)

class Boundary:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.angle_rad = math.atan2(y2 - y1, x2 - x1)
        self.angle_deg = math.degrees(self.angle_rad)

    def get_normal_angle(self):
        return self.angle_deg - 90

    def draw(self, surface):
        pygame.draw.line(surface, WHITE, (self.x1, self.y1), (self.x2, self.y2), 2)