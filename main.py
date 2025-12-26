import pygame
import sys
import math

#custom imports
from Ray import Ray, GREEN, RED
from Boundary import Boundary

#constants
SCREEN_WIDTH: int = 1200
SCREEN_HEIGHT: int = 800
GRAY = (20, 20, 20)

#initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

#define main objects
my_ray = Ray(100, SCREEN_HEIGHT / 2, 0)
boundaries = [
    Boundary(600, 100, 600, 700),
    Boundary(100, 750, 1100, 750),
    Boundary(100, 50, 1100, 50),
    Boundary(1100, 100, 1100, 700)
]

#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #locate mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #point the ray at the mouse
    my_ray.set_direction(mouse_x, mouse_y)

    closest_point = None
    closest_boundary = None
    min_distance = math.inf

    for boundary in boundaries:
        intersection_pt = my_ray.find_intersection(boundary)
        if intersection_pt:
            dx = my_ray.x - intersection_pt[0]
            dy = my_ray.y - intersection_pt[1]
            distance = math.sqrt(dx ** 2 + dy ** 2)
            if distance < min_distance:
                min_distance = distance
                closest_point = intersection_pt
                closest_boundary = boundary

    screen.fill(GRAY)
    for boundary in boundaries:
        boundary.draw(screen)

    if closest_point:
        pygame.draw.line(screen,GREEN,(my_ray.x, my_ray.y),closest_point, 1)
        pygame.draw.circle(screen,RED,closest_point,5)
        refracted_angle = my_ray.calculate_refracted_angle(closest_boundary, 1.5, 1)

        if refracted_angle is not None:
            refracted_ray = Ray(closest_point[0],closest_point[1],refracted_angle)
            refracted_ray.draw(screen)
    else:
        my_ray.draw(screen)

    pygame.display.flip()

    clock.tick(60)