import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED


class Player(CircleShape):
    def __init__(self, x: int, y: int):
        # call parent constructor with PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)

        # rotation field initialized to 0
        self.rotation = 0

    # triangle method you were given (paste exact math)
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # override draw to render the triangle (player looks like a triangle)
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt: float):
        rotation = PLAYER_TURN_SPEED * dt
        self.rotation += rotation

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
