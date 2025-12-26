import math
import pygame

WHITE = (255, 255, 255)
GREEN = (50,255,50)
RED = (255, 50, 50)

class Ray:

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle_deg = angle
        self.angle_rad = math.radians(angle)
        self.direction_x = math.cos(self.angle_rad)
        self.direction_y = math.sin(self.angle_rad)


    def set_direction(self, x: float, y: float):
        """
        Updates the ray's angle to point at a specific (x, y) coordinate.
        """
        self.direction_x = x - self.x
        self.direction_y = y - self.y

        self.angle_rad = math.atan2(self.direction_y, self.direction_x)
        self.angle_deg = math.degrees(self.angle_rad)

        magnitude: float = math.sqrt(self.direction_x ** 2 + self.direction_y ** 2)
        if magnitude > 0:
            self.direction_x /= magnitude
            self.direction_y /= magnitude

    def find_intersection(self, boundary):

        x1 = self.x
        y1 = self.y
        x2 = self.x + self.direction_x
        y2 = self.y + self.direction_y


        x3 = boundary.x1
        y3 = boundary.y1
        x4 = boundary.x2
        y4 = boundary.y2

        determinant = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if determinant == 0:
            return None

        t_num = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
        u_num = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3))
        t = t_num / determinant
        u = u_num / determinant

        if t > 0 and 0 <= u <= 1:
            pt_x = x1 + t * (x2 - x1)
            pt_y = y1 + t * (y2 - y1)
            return (pt_x, pt_y)

        return None

    def calculate_refracted_angle(self, boundary, n1, n2):
        normal_angle = boundary.get_normal_angle()

        diff = self.angle_deg - normal_angle
        while diff <= -180: diff += 360
        while diff > 180: diff -= 360

        if abs(diff) > 90:
            normal_angle += 180

        theta1 = self.angle_deg - normal_angle
        theta1_rad = math.radians(theta1)



        try:
            sin_theta2 = (n1 * math.sin(theta1_rad)) / n2
            theta2_rad = math.asin(sin_theta2)
            theta2 = math.degrees(theta2_rad)
            return  normal_angle + theta2
        except ValueError:
            return None


    def draw(self, surface):
        end_x = self.x + self.direction_x * 2000
        end_y = self.y + self.direction_y * 2000
        pygame.draw.line(surface, GREEN, (self.x, self.y), (end_x, end_y), 1)