from time import perf_counter

from src.player import Player
from src.entity import Entity
import random
import datetime
import csv
import pygame
class Game(Player):
    def __init__(self, name=""):
        super(Game, self).__init__()
        self.start_time: int = perf_counter()
        self.alive_time: int = perf_counter()
        self.score: int = 0
        self.name: str = name
        self.current_highscore: int = 0
        self.game_over = False
        self.entities: list[Entity] = []
        self.max_lives: int = 10
        self.max_entities: int = 5
        self.logo_image: pygame.Surface = pygame.image.load("data\gfx\logo_image.png").convert_alpha()
        self.logo_image: pygame.Surface = pygame.transform.scale(self.logo_image, (200, 200))
        self.updated_scoreboard: bool = False
    def update_player_name(self, name):
        self.name = name

    def add_entity(self):
        random_chance = random.randint(1, 100)
        if random_chance < 5:
            if len(self.entities) >= self.max_entities:
                removed_entity = self.entities.pop(0)  # TODO Implement Removed Entities Have Negative Effect - E.g Thunder Cloud Mario Kart
            entity_id = random.randint(1, 4)
            self.entities.append(Entity(entity_id))

    def update_lives(self, change):
        if self.lives + change <= self.max_lives:
            self.lives += change
        else:
            self.increment_score(10000)  # Bonus for Reaching Max Lives

    def current_alive_time(self):
        current_time: datetime.timedelta = perf_counter()
        self.alive_time: int = round((current_time - self.start_time))

    def get_lives(self, difficulty: str):
        if difficulty == "easy":
            return 5

    def check_player_status(self):
        if self.dead:
            self.game_over = True

    def increment_score(self, increase):
        self.score += increase
        
    def entity_effect(self, entity_type, change):
        if entity_type == "life":
            self.update_lives(change)
        elif entity_type == "speed":
            self.change_speed(change)
        elif entity_type == "score":
            self.increment_score(change)
        else:
            raise("Entity has Unknown Type.")

    def check_collisions_of_entities(self):
        for entity in self.entities:
            touching = entity.check_collision(self.player_rect)
            if touching:
                self.entity_effect(entity.type, entity.change)
                self.entities.remove(entity)

    def write_to_scoreboard(self):
        if not self.updated_scoreboard:
            path = 'data\history\scoreboard.csv'

            time = datetime.datetime.today().isoformat()
            data = {
                "name": self.name,
                "score": self.score,
                "alive_time": self.alive_time,
                "total_jumps": self.total_jumps,
                "timestamp": time,
            }
            field_names = list(data.keys())

            with open(path, 'a+') as scoreboard:
                writer = csv.DictWriter(scoreboard, fieldnames=field_names, lineterminator='\n')
                if scoreboard.tell() == 0:
                    writer.writeheader()
                writer.writerow(data)

            self.updated_scoreboard = True
            pygame.time.wait(200)

    