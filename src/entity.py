from src.metadata import MetaData
import random
import pygame

configurations = {
    "coin": {
        "image": "data\\gfx\\coin.png",
        "gravity": 0,
        "jump_height": 0,
        "speed": 10,
        "effect_time": 10,
        "entity_movement": 0
    },
    "1-up": {
        "image": "data\\gfx\\1-up.png",
        "gravity": 0,
        "jump_height": 0,
        "speed": 10,
        "effect_time": 10,
        "entity_movement": 0
    },
    "zoom_shoes": {
        "image": "data\\gfx\\zoom_shoes.png",
        "gravity": 0,
        "jump_height": 0,
        "speed": 10,
        "effect_time": 10,
        "entity_movement": 0
    },
    "falling_pipe": {
        "image": "data\\gfx\\pipe.png",
        "gravity": 0,
        "jump_height": 0,
        "speed": 10,
        "effect_time": 10,
        "entity_movement": -10
    }
}



class Entity(MetaData):
    def __init__(self, entity_id: str):
        super(Entity, self).__init__()
        self.entity_id = entity_id
        self.get_config()
        self.coord_x = random.randint(20, self.screen_width-20)
        self.coord_y = random.randint(20, self.screen_height-20)
        self.coords = (self.coord_x, self.coord_y)
        self.sprite: pygame.image = pygame.image.load(self.image).convert_alpha()
        self.sprite: pygame.image = pygame.transform.scale(self.sprite, (40, 40))
        
    def get_config(self):
        entity_config = configurations[self.entity_id]
        self.gravity_modifier: int = entity_config["gravity"]
        self.jump_height_modifier: int = entity_config["jump_height"]
        self.speed_modifier: int = entity_config["speed"]
        self.effect_time: int = entity_config["effect_time"]
        self.entity_movement: int = entity_config["entity_movement"]
        self.image: str = entity_config["image"]
