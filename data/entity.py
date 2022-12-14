configurations = {
    "1": {
        "gravity": 0,
        "jump_height": 0,
        "speed": 10,
        "effect_time": 10,
    }
}

class Entity:
    
    def __init__(self, entity_id: str):
        self.entity_id = entity_id
        self.get_config()
        
    def get_config(self):
        entity_config = configurations[self.entity_id]
        self.gravity_modifier = entity_config["gravity"]
        self.jump_height_modifier = entity_config["jump_height"]
        self.speed_modifier = entity_config["speed"]
        self.effect_time = entity_config["effect_time"]