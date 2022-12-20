from src.metadata import MetaData
import random
import pygame

configurations = {
    "1": {
        "image": "data\\gfx\\coin.png",
        "gravity": 0,
        "jump_height": 0,
        "speed": 10,
        "effect_time": 10,
        "entity_movement": 0,
        "score_change": 1000,
        "life_change": 0,
    },
    "2": {
        "image": "data\\gfx\\1-up.png",
        "gravity": 0,
        "jump_height": 0,
        "speed": 10,
        "effect_time": 10,
        "entity_movement": 0,
        "score_change": 0,
        "life_change": 1,
    },
    "3": {
        "image": "data\\gfx\\zoom_shoes.png",
        "gravity": 0,
        "jump_height": 0,
        "speed": 10,
        "effect_time": 10,
        "entity_movement": 0,
        "score_change": 1000,
        "life_change": 0,
    },
    # "4": {
    #     "image": "data\\gfx\\pipe.png",
    #     "gravity": 0,
    #     "jump_height": 0,
    #     "speed": 10,
    #     "effect_time": 10,
    #     "entity_movement": -10
    # }
}


class Entity(MetaData):
    def __init__(self, entity_id: str):
        super(Entity, self).__init__()
        self.entity_id = entity_id
        self.entity_width = 40
        self.entity_height = 40
        self.get_config()
        self.coord_x = random.randint(20, self.screen_width - 20)
        self.coord_y = random.randint(20, self.screen_height - 20)
        self.coords = (self.coord_x, self.coord_y)
        self.sprite: pygame.image = pygame.image.load(self.image).convert_alpha()
        self.sprite: pygame.image = pygame.transform.scale(self.sprite, (self.entity_width, self.entity_height))
        self.rect: pygame.rect = self.sprite.get_rect(topleft=(self.get_position()))

    def get_position(self):
        return (self.coord_x, self.coord_y)

    def get_config(self):
        entity_config = configurations[str(self.entity_id)]
        self.gravity_modifier: int = entity_config["gravity"]
        self.jump_height_modifier: int = entity_config["jump_height"]
        self.speed_modifier: int = entity_config["speed"]
        self.effect_time: int = entity_config["effect_time"]
        self.entity_movement: int = entity_config["entity_movement"]
        self.image: str = entity_config["image"]
        self.score_change: int = entity_config["score_change"]
        self.life_change: int = entity_config["life_change"]

    def check_collision(self, player_rect):
        if player_rect.colliderect(self.rect):
            return True
        else:
            return False
