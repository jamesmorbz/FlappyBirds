from time import perf_counter

from data.player import Player


class Game(Player):
    def __init__(self):
        super(Game, self).__init__()
        self.start_time: int = perf_counter()
        self.score: int = 0
        self.name: str = ""
        self.current_highscore: int = 0

    def update_player_name(self, name):
        self.name = name

    def update_lives(self, lives):
        self.lives = lives

    def current_alive_time(self):
        current_time: int = perf_counter()
        alive_time: int = current_time - self.start_time
        return alive_time

    def get_lives(self, difficulty: str):
        if difficulty == "easy":
            return 5

    def check_player_status(self):
        if self.lives == 0:
            self.playing = False

    def increment_score(self, increase):
        self.score += increase
