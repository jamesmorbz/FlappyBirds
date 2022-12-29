import json
import pygame
from pygame.locals import BUTTON_LEFT, K_ESCAPE, K_SPACE, KEYDOWN, RESIZABLE
import sys
import names
import os
import logging

def read_config():
    try:
        with open ("data\history\config.json") as config_file:
            config = json.load(config_file)
    except:
        config = {}

    return config        

def write_config(data: dict = None):
    if data is None:
        with open ("data\history\config.json") as config_file:
            data = json.load(config_file)
    with open("data\history\config.json", "w") as config_file:
        json.dump(data, config_file)


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


def get_random_name():
    return names.get_full_name()


def default_config_creation():
    path = "data\history\config.json"
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

def exit_game():
    pygame.quit()
    sys.exit()
