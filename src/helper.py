import json
import pygame
from pygame.locals import BUTTON_LEFT, K_ESCAPE, K_SPACE, KEYDOWN, RESIZABLE
import sys
import os
import logging
import pandas as pd
import csv

def read_config():
    try:
        with open("data\history\config.json", "r") as config_file:
            config = json.load(config_file)
    except:
        config = {}

    return config        

def write_config(new_data: dict = None):
    with open("data\history\config.json", "r+") as config:
        data = json.load(config)

        new_config = data | new_data

        config.seek(0)
        json.dump(new_config, config)
        config.truncate()


def diff_tuples(tuple1, tuple2):
    return tuple(map(lambda i, j: i - j, tuple1, tuple2))


def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def default_config_creation():
    path = "data\history\config.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    default_config =     {
                "load_with_splash_screen": True,
                "write_scoreboard": True,
                "background_colour": [81,159,204],
                "game_over_colour": [200,95,255]
                }
    if os.path.exists(path):
        logging.info("Config Already Exists.")
    else:
        logging.info("Creating Config...")
        with open(path, "w") as config:
            json.dump(default_config, config)

def get_current_highscore():
    path = "data\history\scoreboard.csv"
    high_score_string = "HIGHSCORE"
    if not os.path.exists(path):
        return f"{high_score_string}: NOT SET"
    else:
        with open(path, "r") as scoreboard:
            scorereader = csv.DictReader(scoreboard, delimiter=',')
            high_score = max([row for row in scorereader], key=lambda x: float(x["score"]))
        score = high_score["score"]
        player = high_score["name"]
        score = high_score["score"]
        timestamp = high_score["timestamp"]
        jumps = high_score["total_jumps"]
        return f"{high_score_string}: {score} in ({jumps} jumps) by {player} @ {timestamp}"

def exit_game():
    pygame.quit()
    sys.exit()
