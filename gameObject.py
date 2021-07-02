import pygame
class GameObject:
    def __init__(self, x, y, width, height, image_path):
        """loads the image from the path"""
        image = pygame.image.load(image_path)
        """scales the image to the dimensions in a new variable"""
        self.image = pygame.transform.scale(image, (width, height))

        #setting input values as accessible properties
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image_path = image_path

    def flip(self):
        if '_r' in self.image_path:
            self.image_path = self.image_path.replace('_r.png', '.png')
        else:
            self.image_path = self.image_path.replace('.png', '_r.png')
        image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(image, (self.width, self.height))

    def change_image(self, image_path):
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image, (self.width, self.height))
