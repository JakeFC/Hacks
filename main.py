import pygame

"""first step to do anything with pygame"""
pygame.init()

"""dimensions of the window"""
width = 1080
height = 720
"""tuple of r,g, b values"""
white_color = (255, 255, 255)

"""sets dimensions with tuple"""
game_window = pygame.display.set_mode((width, height))

"""keeps track of time for the game loop"""
clock = pygame.time.Clock()

def run_game_loop():
    """game loop"""
    while True:

        # handle events
        """gets a list of all events simultaneously"""
        events = pygame.event.get()
        for event in events:
            """ends the game loop if QUIT event occurs"""
            if event.type == pygame.QUIT:
                return

        # execute logic
        # update display
        """sets background color"""
        game_window.fill(white_color)
        """updates the graphics to the window"""
        pygame.display.update()

        """sets loop rate at 60 loops per second"""
        clock.tick(60)

run_game_loop()

"""ends pygame"""
pygame.quit()

"""ends script"""
quit()