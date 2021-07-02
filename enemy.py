import pygame
from gameObject import GameObject
class Enemy(GameObject):

    """subclass of GameObject"""
    def __init__(self, x, y, width, height, image_path, speed):
        """initializes the GameObject-defined properties in parent class"""
        super().__init__(x, y, width, height, image_path)
        """speed (and direction) when moving"""
        self.speed = speed

    def move(self, max_width):
        if self.x <= 0:
            """if enemy hits left, change speed to right"""
            self.speed = abs(self.speed)
            self.flip()

        if self.x >= (max_width - self.width):
            """if enemy hits right, change speed to left"""
            self.speed = -self.speed
            self.flip()

        #if self.x < 180 or self.x > (max_width - 180 -self.width):
            #self.change_image('assets/blank.png')
        #else:
            #self.change_image('assets/enemy.png')

        """move x position by speed(and direction)"""
        self.x += self.speed
