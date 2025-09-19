import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED


class Player(CircleShape):

    def __init__(self, x: int, y: int, updatables, drawables):
        # call parent constructor with PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)

        # rotation field initialized to 0
        self.rotation = 0

        updatables.append(self)
        drawables.append(self)

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
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt: float):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
