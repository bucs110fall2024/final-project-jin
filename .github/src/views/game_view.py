import pygame
import os
import random

class GameView:
    def __init__(self, screen):
        self.screen = screen
        # Set image path based on current file location
        base_path = os.path.dirname(os.path.abspath(__file__))
        archer_image_path = os.path.join(base_path, '../../assets/images/archer.png')
        target_image_path = os.path.join(base_path, '../../assets/images/target.png')

        # Load and resize images
        original_archer_image = pygame.image.load(archer_image_path)
        self.archer_image = pygame.transform.scale(original_archer_image, (50, 50))  # Resize archer image to 50x50

        original_target_image = pygame.image.load(target_image_path)
        self.target_image = pygame.transform.scale(original_target_image, (40, 40))  # Resize target image to 40x40

        # Initialize archer position to center
        self.archer_x = (screen.get_width() // 2) - 25  # Set archer's horizontal position to the center of the screen
        self.archer_y = (screen.get_height() // 2) + 100  # Set archer's vertical position towards the bottom of the screen

        # Initialize target position to top center
        self.target_x = (screen.get_width() // 2) - 20  # Set target's horizontal position to the center of the screen
        self.target_y = (screen.get_height() // 2) - 200  # Set target's vertical position towards the top of the screen

        # Initialize arrow list
        self.arrows = []

        # Initialize score
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)
        self.hit_message = ''
        self.hit_message_timer = 0

        # Initialize wind variables
        self.wind_strength = 0
        self.wind_direction = ''
        self.next_wind_strength = random.uniform(-6, 6)

    def shoot_arrow(self, wind_strength):
        # Set initial position of the arrow and add it to the list
        arrow_rect = pygame.Rect(self.archer_x + 20, self.archer_y, 5, 10)
        self.arrows.append({'rect': arrow_rect, 'wind': wind_strength})

        # Set current wind direction to the next wind direction and generate new next wind
        self.set_wind_direction(self.next_wind_strength)
        self.next_wind_strength = random.uniform(-6, 6)

    def set_wind_direction(self, wind_strength):
        # Set wind direction
        self.wind_strength = wind_strength
        if wind_strength < 0:
            self.wind_direction = 'left'
        elif wind_strength > 0:
            self.wind_direction = 'right'
        else:
            self.wind_direction = 'none'

    def update(self):
        # Draw background
        self.screen.fill((255, 255, 255))  

        # Draw target
        self.screen.blit(self.target_image, (self.target_x, self.target_y))

        # Draw archer
        self.screen.blit(self.archer_image, (self.archer_x, self.archer_y))

        # Draw and move arrows
        for arrow in self.arrows[:]:
            arrow['rect'].y -= 5 
            arrow['rect'].x += arrow['wind'] 
            pygame.draw.rect(self.screen, (0, 0, 0), arrow['rect']) 

            # Check if the arrow hits the target
            if self.target_x < arrow['rect'].x < self.target_x + 40 and self.target_y < arrow['rect'].y < self.target_y + 40:
                self.arrows.remove(arrow)
                self.score += 1
                self.hit_message = 'HIT!'
                self.hit_message_timer = 30

        # Display score
        score_text = self.font.render(f'Score: {self.score}', True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))

        # Display hit message
        if self.hit_message_timer > 0:
            hit_text = self.font.render(self.hit_message, True, (255, 0, 0))
            self.screen.blit(hit_text, (self.screen.get_width() // 2 - 50, self.screen.get_height() // 2))
            self.hit_message_timer -= 1

        # Display next wind information
        if abs(self.next_wind_strength) < 2:
            wind_strength_label = 'weak wind'
        else:
            wind_strength_label = 'strong wind'

        if self.next_wind_strength < 0:
            wind_direction_label = 'left'
        elif self.next_wind_strength > 0:
            wind_direction_label = 'right'
        else:
            wind_direction_label = 'none'

        wind_text = self.font.render(f'Next Wind: {wind_direction_label}, {wind_strength_label}', True, (0, 0, 0))
        self.screen.blit(wind_text, (10, self.screen.get_height() - 40))
