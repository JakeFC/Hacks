import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy
class Game:
    """the game"""
    def __init__(self):
        """dimensions of the window"""
        self.width = 1080
        self.height = 720
        """tuple of r,g, b values"""
        self.white_color = (255, 255, 255)
        """sets dimensions with tuple"""
        self.game_window = pygame.display.set_mode((self.width, self.height))
        """keeps track of time for the game loop"""
        self.clock = pygame.time.Clock()
        """sets the background object at 0, 0(x, y) and scales the dimensions to the game window"""
        self.background = GameObject(0, 0, self.width, self.height, 'assets/background.png')
        """sets the treasure image at 506, 45(x, y) and scales the dimensions to 68x45 px"""
        self.treasure = GameObject(494, 37, 92, 61, 'assets/treasure.png')
        """starting level to change difficulty off of"""
        self.level = 1.0
        """creates the player and enemies at the start"""
        self.reset_map()
    def reset_map(self):
        """on level change, redraws players and enemies at new position with speed change"""
        speed = 2 * (self.level * 5)
        """sets the player image at 506, 630(x, y) and scales to 68x45 px with small variable speed increase"""
        self.player = Player(506, 660, 68, 45, 'assets/player.png', 4 + speed / 9)
        """sets the enemy images at x, y and scales to 68x45 px at variable speed"""
        if self.level >= 2.0:
            self.enemies = [
                Enemy(0, 180, 68, 45, 'assets/enemy.png', speed),
                Enemy(1012, 360, 68, 45, 'assets/enemy.png', speed),
                Enemy(0, 540, 68, 45, 'assets/enemy.png', speed),
            ]
        elif self.level >= 1.5:
            self.enemies = [
                Enemy(0, 180, 68, 45, 'assets/enemy.png', speed),
                Enemy(1012, 360, 68, 45, 'assets/enemy.png', speed),
            ]
        else:
            self.enemies = [
                Enemy(0, 180, 68, 45, 'assets/enemy.png', speed),
            ]
    def draw_objects(self):
        """does what it says"""
        """sets background color"""
        self.game_window.fill(self.white_color)
        """draws the background image at the x,y position"""
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        #display the images at x,y
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        """draw the list of enemies at x, y"""
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
        """updates the graphics to the window"""
        pygame.display.update()
    def move_objects(self, player_direction_y, player_direction_x):
        """move the player and enemy every iteration"""
        self.player.move(player_direction_y, player_direction_x, self.height, self.width)
        for enemy in self.enemies:
            enemy.move(self.width)
    def detect_collision(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            """if obj 1 is under bottom of obj 2"""
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            """if obj 2 is above top of obj 1"""
            return False
        if object_1.x > (object_2.x + object_2.width):
            """if obj 1 is right of the right side of obj 2"""
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            """if obj 2 is right of the right side of obj 1"""
            return False
        return True
    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.level = 1.0
                return True
        if self.detect_collision(self.player, self.treasure):
            self.level += 0.5
            return True
        return False
    def run_game_loop(self):
        """the never-ending loop that is our game"""
        player_direction_y = 0
        player_direction_x = 0
        while True:
            # handle events
            """gets a list of all events simultaneously"""
            events = pygame.event.get()
            for event in events:
                """ends the game loop if QUIT event occurs"""
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    """if a key is pushed down"""
                    if event.key == pygame.K_UP:
                        """negative direction lowers y position(goes up)"""
                        player_direction_y -= 1
                    if event.key == pygame.K_DOWN:
                        """positive direction raises y position(goes down)"""
                        player_direction_y += 1
                    if event.key == pygame.K_LEFT:
                        """negative direction lowers x position(goes left)"""
                        player_direction_x -= 1
                    if event.key == pygame.K_RIGHT:
                        """positive direction raises x position(goes right)"""
                        player_direction_x += 1
                elif event.type == pygame.KEYUP:
                    """if a key is lifted up"""
                    if event.key == pygame.K_UP:
                        player_direction_y += 1
                    if event.key == pygame.K_DOWN:
                        player_direction_y -= 1
                    if event.key == pygame.K_LEFT:
                        player_direction_x += 1
                    if event.key == pygame.K_RIGHT:
                        player_direction_x -= 1
            # execute logic
            self.move_objects(player_direction_y, player_direction_x)
            # update display
            """draw the objects every iteration"""
            self.draw_objects()
            # detect collisions
            if self.check_if_collided():
                self.reset_map()
            """sets loop rate at 60 loops per second"""
            self.clock.tick(60)            