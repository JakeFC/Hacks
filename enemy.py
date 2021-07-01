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
            #self.change_image('assets/enemy.png')
        if self.x >= (max_width - self.width):
            """if enemy hits right, change speed to left"""
            self.speed = -self.speed
            #self.change_image('assets/player.png')
        """move x position by speed(and direction)"""
        self.x += self.speed
# from gameObject import GameObject

# class Enemy(GameObject):


#     def __init__(self, x, y, width, height, image_path, speed):
#         super().__init__(x, y, width, height, image_path)

#         self.speed = speed

    
#     def move(self, max_width):
#         if self.x <= 0:
#             self.speed = abs(self.speed)
#         elif self.x >= max_width - self.width:
#             self.speed = -self.speed

#         self.x += self.speed
        