import pygame
from src.views.game_view import GameView
import random
import sys

class GameController:
    def __init__(self):
        # Initialize Pygame screen
        self.screen = pygame.display.set_mode((800, 600))
        self.view = GameView(self.screen)
        self.running = True

        # Initialize wind variable
        self.wind_strength = random.uniform(-2, 2)  # Random wind strength between -2 and 2

        # Track number of attempts
        self.attempts = 0
        self.max_attempts = 5  # Maximum number of attempts allowed

    def start_menu(self):
        # Display start menu
        self.screen.fill((255, 255, 255))
        font = pygame.font.SysFont(None, 48)
        title_text = font.render("Archery Game", True, (0, 0, 0))
        start_text = font.render("Press SPACE to Start", True, (0, 0, 0))

        self.screen.blit(title_text, (self.screen.get_width() // 2 - title_text.get_width() // 2, 200))
        self.screen.blit(start_text, (self.screen.get_width() // 2 - start_text.get_width() // 2, 300))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False

    def end_menu(self):
        # Display end menu
        self.screen.fill((255, 255, 255))
        font = pygame.font.SysFont(None, 48)
        end_text = font.render(f"Game Over! Final Score: {self.view.score}", True, (0, 0, 0))
        restart_text = font.render("Press R to Restart or Q to Quit", True, (0, 0, 0))

        self.screen.blit(end_text, (self.screen.get_width() // 2 - end_text.get_width() // 2, 200))
        self.screen.blit(restart_text, (self.screen.get_width() // 2 - restart_text.get_width() // 2, 300))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.view = GameView(self.screen)  # Reset the game view for a new game
                        self.attempts = 0  # Reset attempts
                        waiting = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

    def run(self):
        # Start the game with the start menu
        self.start_menu()

        # Main game loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                # Shoot arrow on mouse click
                if event.type == pygame.MOUSEBUTTONDOWN and self.attempts < self.max_attempts:
                    self.view.shoot_arrow(self.wind_strength)
                    self.attempts += 1  # Increment the number of attempts
                    # Change wind strength after each shot
                    self.wind_strength = random.uniform(-6, 6)

            # Handle key input (move archer left or right)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.view.archer_x > 0:
                self.view.archer_x -= 0.3
            if keys[pygame.K_RIGHT] and self.view.archer_x < 740:
                self.view.archer_x += 0.3

            # Update screen
            self.view.update()
            pygame.display.flip()

            # Check if the game should end after max attempts
            if self.attempts >= self.max_attempts:
                self.end_menu()

        pygame.quit()
