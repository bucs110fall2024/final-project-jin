import os
import sys
import pygame

# Set project root path
base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_path, 'src'))

from src.controllers import game_controller

# Import required classes
GameController = game_controller.GameController

# Set the working directory based on the current file location
os.chdir(base_path)
print("Current Working Directory:", os.getcwd())  # Debugging log

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Archery Game")

    # Initialize GameController
    controller = GameController()
    controller.run()

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
