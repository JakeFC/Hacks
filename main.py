import pygame
from game import Game

"""first step to do anything with pygame"""
pygame.init()
pygame.font.init()
pygame.mixer.init()

game = Game()
game.run_game_loop()

"""ends pygame"""
pygame.quit()

"""ends script"""
quit()
