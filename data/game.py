from time import perf_counter
from data.player import Player
from data.metadata import MetaData
from data.entity import Entity

class Game:
    def __init__(self, metadata: MetaData, name: str, difficulty: str):
        self.start_time: int = perf_counter()
        self.score: int = 0
        self.name: str = name
        self.current_highscore: int = 0
        self.lives: int = self.get_lives(difficulty)
        player = Player(metadata)
        self.allsprites: tuple[Player, Entity] = (player)
        self.player: Player = player

    def current_alive_time(self):
        current_time: int = perf_counter()
        alive_time: int = current_time - self.start_time
        return alive_time

    def get_lives(self, difficulty: str):
        if difficulty == "easy":
            return 5
        
    def check_player_status(self):
        if self.player.lives == 0:
            self.playing = False