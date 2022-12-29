import pygame

from src.metadata import MetaData


class Player(MetaData):
    def __init__(self):
        super(Player, self).__init__()
        self.dead = False
        self.is_jumping = False
        self.double_jumping = False
        self.jump_steps = 10
        self.position = pygame.Vector2()
        self.player_width: int = 38
        self.player_height: int = 51
        self.direction: int = 1
        self.distance: int = 0
        self.coord_y: int = self.screen_height / 2
        self.coord_x: int = self.screen_width / 2
        self.gravity: int = -0.1
        self.jump_height: int = 20
        self.speed: int = 200
        self.right_player_sprite: pygame.image = pygame.image.load("data\gfx\\right_bird.png").convert_alpha()
        self.left_player_sprite: pygame.image = pygame.image.load("data\gfx\left_bird.png").convert_alpha()
        self.refresh_sprite()
        self.lives = 1
        self.total_jumps = 0
        self.heart_image: pygame.Surface = pygame.image.load("data\gfx\heart.png").convert_alpha()
        self.heart_image: pygame.Surface = pygame.transform.scale(self.heart_image, (40, 40))

    def get_position(self):
        return (self.coord_x, self.coord_y)

    def scale_sprite(self, sprite):
        return pygame.transform.scale(sprite, (self.player_width, self.player_height))

    def get_sprite(self):
        if self.direction == 1:
            return self.right_player_sprite
        if self.direction == -1:
            return self.left_player_sprite

    def change_lives(self, change):
        self.lives += change

    def update(self, td):
        if self.lives <= 0:
            self.dead = True

        if self.is_jumping:
            # if self.double_jumping:
            #     self.total_jumps += 1
            #     self.jump_steps = 10
            #     self.double_jumping_applied = False
            if self.jump_steps >= -10:
                self.coord_x += abs(self.jump_steps) * self.direction * (self.speed * td)
                self.coord_y -= (self.jump_steps * abs(self.jump_steps)) * (self.jump_height / 50) - ((self.gravity / (10 * td)))
                self.jump_steps -= 1
            else:
                self.jump_steps = 10
                self.reset_jump()
        else:
            self.coord_x = (self.direction * (self.speed * td)) + self.coord_x
            self.coord_y = self.coord_y - ((self.gravity / (10 * td)))

        self.check_window_boundary_collisions()
        self.refresh_sprite()

    def refresh_sprite(self):
        self.image: pygame.Surface = self.scale_sprite(self.get_sprite())
        self.player_rect: pygame.rect = self.image.get_rect(topleft=(self.get_position()))

    def check_window_boundary_collisions(self):
        if self.coord_x > (self.screen_width - self.image.get_size()[0]):
            self.direction = -1

        if self.coord_x < 0:
            self.direction = 1

        if self.coord_y > self.screen_height:
            self.change_lives(-1)
            if self.lives > 0:
                self.reset_player_position()

        if self.coord_y <= -1:
            self.coord_y == 0

    def reset_player_position(self):
        self.coord_y = self.screen_height / 2
        self.coord_x = self.screen_width / 2

    def revive_sprite(self):
        self.dead = False

    def kill_sprite(self):
        self.dead = True

    def reset_jump(self):
        self.is_jumping = False
        self.double_jumping = False

    def jump(self):
        if self.is_jumping and not self.double_jumping:
            self.double_jumping = True
        elif not self.is_jumping:
            self.total_jumps += 1
            self.is_jumping = True

    def change_speed(self, change):
        self.speed = self.speed + change

    def change_gravity(self, change):
        self.gravity = self.gravity + change

    def change_jump_height(self, change):
        self.jump_height = self.jump_height + change
