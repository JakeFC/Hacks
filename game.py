import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy
from random import randint

class Game:
    """the game"""

    def __init__(self):
        """dimensions of the window"""
        self.width = 800
        self.height = 800
        """tuple of r,g, b values"""
        self.white_color = (255, 255, 255)

        """sets dimensions with tuple"""
        self.game_window = pygame.display.set_mode((self.width, self.height))

        """keeps track of time for the game loop"""
        self.clock = pygame.time.Clock()

        """sets the background object at 0, 0(x, y) and scales the dimensions to the game window"""
        self.background = GameObject(0, 0, self.width, self.height, 'assets/snow.png')

        """passing tree_width and tree_height into int() function because khorne wants it or gameObjects require an int"""
        self.tree_width = int(self.width / 12)
        self.tree_height = int(self.height / 4)

        """coordinates for all the tree images"""
        tree_coords = [(0, -self.tree_height / 2), (self.tree_width, -self.tree_height / 2), (self.tree_width * 2, -self.tree_height / 2), ((self.width - (self.tree_width * 3)), -self.tree_height / 2), (self.width - (self.tree_width * 2), -self.tree_height / 2), (self.width - self.tree_width, -self.tree_height / 2),
                       (0, 0), (self.tree_width, 0), (self.width - (self.tree_width * 2), 0), (self.width - self.tree_width, 0),
                       (0, (self.tree_height / 2)), (self.tree_width, (self.tree_height / 2)), (self.width - (self.tree_width * 2), (self.tree_height / 2)), (self.width - self.tree_width, (self.tree_height / 2)),
                       (0, (self.tree_height)), (self.tree_width, (self.tree_height)), (self.width - (self.tree_width * 2), (self.tree_height)), (self.width - self.tree_width, (self.tree_height)),
                       (0, (self.tree_height * 1.5)), (self.tree_width, (self.tree_height * 1.5)), (self.width - (self.tree_width * 2), (self.tree_height * 1.5)), (self.width - self.tree_width, (self.tree_height * 1.5)),
                       (0, (self.tree_height * 2)), (self.tree_width, (self.tree_height * 2)), (self.width - (self.tree_width * 2), (self.tree_height * 2)), (self.width - self.tree_width, (self.tree_height * 2)),
                       (0, (self.tree_height * 2.5)), (self.tree_width, (self.tree_height * 2.5)), (self.width - (self.tree_width * 2), (self.tree_height * 2.5)), (self.width - self.tree_width, (self.tree_height * 2.5)),
                       (0, (self.tree_height * 3)), (self.tree_width, (self.tree_height * 3)), (self.width - (self.tree_width * 2), (self.tree_height * 3)), (self.width - self.tree_width, (self.tree_height * 3)),
        ]

        self.trees = []
        """list of tree game objects created"""
        for coord in tree_coords:
            """adding Christmas spirit"""
            self.trees.append(GameObject(coord[0], coord[1], self.tree_width, self.tree_height, 'assets/tree_' + str(randint(1, 5)) + '.png'))

        self.entity_width = int(self.width / 16)
        self.entity_height = int(self.height / 16)

        """sets the padoru image at 471, 22(x, y) and scales the dimensions to self.entity_width * self.entity_height px"""
        self.padoru = GameObject((self.width / 2) - self.entity_width, self.height / 32.73, self.entity_width * 2, self.entity_height * 2, 'assets/padoru.png')

        """starting level to change difficulty off of"""
        self.level = 1.0

        """creates the player and enemies at the start"""
        self.reset_map()

    def reset_map(self):
        """on level change, redraws players and enemies at new position with speed change"""

        speed = (self.height / 360) * (self.level * 3)
        """sets the player image at 506, 630(x, y) and scales to self.entity_width * self.entity_height px with small variable speed increase"""
        self.player = Player((self.width / 2) - (self.entity_width / 2), (self.height / 1.09), self.entity_width, self.entity_height, 'assets/player.png', (self.height / 180) + speed / (self.height / 100))

        """sets the enemy images at x, y and scales to self.entity_width * self.entity_height px at variable speed"""
        if self.level >= 4.0:
            self.enemies = [
                Enemy(0, (self.entity_height * 4), self.entity_width, self.entity_height, 'assets/pado_green_r.png', speed),
                Enemy(int(self.width - self.entity_width), (self.entity_height * 8), self.entity_width, self.entity_height, 'assets/pado_pink.png', speed),
                Enemy(0, (self.entity_height * 12), self.entity_width, self.entity_height, 'assets/pado_blue_r.png', speed),
            ]
        elif self.level >= 2.0:
            self.enemies = [
                Enemy(0, (self.entity_height * 4), self.entity_width, self.entity_height, 'assets/pado_green_r.png', speed),
                Enemy(int(self.width - self.entity_width), (self.entity_height * 8), self.entity_width, self.entity_height, 'assets/pado_pink.png', speed),
            ]
        else:
            self.enemies = [
                Enemy(0, (self.entity_height * 4), self.entity_width, self.entity_height, 'assets/pado_green_r.png', speed),
            ]

    def draw_objects(self):
        """does what it says"""
        """sets background color"""
        self.game_window.fill(self.white_color)

        """draws the background image at the x,y position"""
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        #display the images at x,y
        self.game_window.blit(self.padoru.image, (self.padoru.x, self.padoru.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))

        """draw the list of enemies at x, y"""
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
        """draw the list of trees after at x, y"""
        for tree in self.trees:
            self.game_window.blit(tree.image, (tree.x, tree.y))

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
        if self.detect_collision(self.player, self.padoru):
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
                        self.player.change_image('assets/player.png')
                    if event.key == pygame.K_DOWN:
                        """positive direction raises y position(goes down)"""
                        player_direction_y += 1
                        self.player.change_image('assets/down.png')
                    if event.key == pygame.K_LEFT:
                        """negative direction lowers x position(goes left)"""
                        player_direction_x -= 1
                        self.player.change_image('assets/left.png')
                    if event.key == pygame.K_RIGHT:
                        """positive direction raises x position(goes right)"""
                        player_direction_x += 1
                        self.player.change_image('assets/right.png')

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
