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
    def change_image(self, image_path):
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image, (self.width, self.height))
        
# import pygame

# class GameObject:

#     def __init__(self, x, y, width, height, image_path):
#         image = pygame.image.load(image_path)
#         self.image = pygame.transform.scale(image, (width, height))

#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height

