from src.metadata import MetaData
import random
import pygame

configurations = {
    "1": {
        "image": "data\gfx\coin.png",
        "type": "score",
        "change": 1000,
        "effect_time": 0,
    },
    "2": {
        "image": "data\gfx\\1-up.png",
        "type": "life",
        "change": 1,
        "effect_time": 0,
    },
    "3": {
        "image": "data\gfx\zoom_shoes.png",
        "type": "speed",
        "change": 10,
        "effect_time": 10,
    },
    "4": {
        "image": "data\gfx\pipe.png",
        "type": "life",
        "change": -1,
        "effect_time": 0,
    }
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
        self.rect: pygame.Rect = self.sprite.get_rect(topleft=(self.get_position()))

    def get_position(self):
        return (self.coord_x, self.coord_y)

    def get_config(self):
        entity_config = configurations[str(self.entity_id)]
        self.image: str = entity_config["image"]
        self.type: int = entity_config["type"]
        self.change: int = entity_config["change"]
        self.effect_time: int = entity_config["effect_time"]

    def check_collision(self, player_rect: pygame.Rect):
        if self.rect.colliderect(player_rect):
            return True
        else:
            return False
