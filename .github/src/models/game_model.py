import random

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

    def move(self, direction):
        self.x += direction * self.speed


class Arrow:
    def __init__(self, x, y, power, wind_effect):
        self.x = x
        self.y = y
        self.vx = power + wind_effect
        self.vy = -power

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.5


class Target:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def reset_position(self):
        self.x = random.randint(100, 700)
        self.y = random.randint(50, 300)


class Wind:
    def __init__(self):
        self.direction = random.choice([-1, 1])
        self.strength = random.uniform(0, 5)

    def update(self):
        self.direction = random.choice([-1, 1])
        self.strength = random.uniform(0, 5)

    def get_effect(self):
        return self.direction * self.strength
