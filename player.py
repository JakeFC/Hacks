from gameObject import GameObject
class Player(GameObject):
    """subclass of GameObject for players"""

    def __init__(self, x, y, width, height, image_path, speed):
        """initializes the GameObject-defined properties in parent class"""
        super().__init__(x, y, width, height, image_path)
        """speed when moving"""
        self.speed = speed

    def move(self, direction_y, direction_x, max_height, max_width):
        x = True
        y = True

        if self.y >= (max_height - self.height) and direction_y > 0:
            """if player bottom is at the bottom and trying to go down, stop"""
            y = False
        if self.y <= (self.height * 2) and direction_y < 0:
            """if player top is at the top and trying to go up, stop"""
            y = False
        if self.x >= ((max_width / 2) + (max_width / 3) - self.width) and direction_x > 0:
            """if player right is at the right and trying to go right, stop"""
            x = False
        if self.x <= (max_width / 2) - (max_width / 3) and direction_x < 0:
            """if player left is at the left and trying to go left, stop"""
            x = False

        if y:
            """y position value gets lower for up and higher for down * speed"""
            self.y += (direction_y * self.speed)
        if x:
            """x position value gets lower for left and higher for down * speed"""
            self.x += (direction_x * self.speed)
