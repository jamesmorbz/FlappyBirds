import sys

import pygame
from pygame.locals import BUTTON_LEFT, K_ESCAPE, K_SPACE, KEYDOWN, RESIZABLE

from src.colours import Colours
from src.game import Game
from src.metadata import MetaData
from src.entity import Entity
import names


def diff_tuples(tuple1, tuple2):
    return tuple(map(lambda i, j: i - j, tuple1, tuple2))


def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


def get_random_name():
    return names.get_full_name()

def main():
    splash_screen = False
    MainMenu = False
    MainGame = True
    score_written = False

    display = pygame.display.set_mode((metadata.screen_size), RESIZABLE)

    pygame.display.set_caption("Flappy Pong")

    background = pygame.image.load("data\\gfx\\background.png")
    heart_image = pygame.image.load("data\\gfx\\heart.png").convert_alpha()
    heart_image = pygame.transform.scale(heart_image, (40, 40))

    logo_image = pygame.image.load("data\\gfx\\logo_image.png").convert_alpha()
    pygame.display.set_icon(logo_image)
    logo_image = pygame.transform.scale(logo_image, (200, 200))

    game = Game()
    game.update_player_name(get_random_name())

    logo_text_y_coord = 30

    while True:
        if splash_screen:
            td = clock.tick(60)
            display.fill(Colours.Black)
            display.blit(background, (0, 0))
            logo_text = pygame.image.load("data\\gfx\\logo_text.png")
            logo_text_w, logo_h = logo_text.get_size()
            logo_image_w, logo_image_h = logo_image.get_size()
            display.blit(logo_text,((metadata.screen_width / 2) - (logo_text_w / 2), logo_text_y_coord))
            display.blit(logo_image,((metadata.screen_width / 2) - (logo_image_w / 2),logo_text_y_coord - logo_image_h - 5,))
            logo_text_y_coord = logo_text_y_coord + (15 / td)

            if logo_text_y_coord > metadata.screen_height:
                splash_screen = False

            check_for_exit()

        if not splash_screen and not game.game_over:
            td = clock.tick(60)
            td = td / 1000  # Convert milliseconds to seconds

            display.fill(Colours.Black)
            display.blit(background, (0, 0))

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        game.jump()
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game.jump()

            current_score_text = SMALL_FONT.render(str(game.score), True, Colours.Black)
            total_jumps = BIG_FONT.render(str(game.total_jumps), True, Colours.Black)
            total_jumps.set_alpha(127)

            display.blit(current_score_text, diff_tuples(game.screen_size,current_score_text.get_size()))
            total_jumps_w,total_jumps_h = total_jumps.get_size()
            display.blit(total_jumps, ((game.screen_width / 2) - total_jumps_w, (game.screen_height / 2) - total_jumps_h))

            game.update(td)
            game.add_entity()
            game.check_collisions_of_entities()
            game.check_player_status()
            game.increment_score(1)
            game.current_alive_time()

            display.blit(game.image, game.get_position())

            for entity in game.entities:
                display.blit(entity.sprite, (entity.coords))

            for i in range(0, game.lives):
                x, y = heart_image.get_size()
                display.blit(heart_image, (i * x, game.screen_height - y))

        if game.game_over:
            display.fill(Colours.Red)
            game_over = SMALL_FONT.render(f"GAME OVER {game.name}. You Scored {game.score}", True, Colours.White)
            display.blit(game_over, diff_tuples(game.screen_size, game_over.get_size()))
            if not score_written:
                game.write_to_scoreboard()
                score_written = True
            check_for_exit()

        pygame.display.update()

if __name__ == "__main__":
    metadata = MetaData()
    pygame.init()
    clock = pygame.time.Clock()
    SMALL_FONT = pygame.font.Font("data\\font\\font.otf", 36)
    BIG_FONT = pygame.font.Font("data\\font\\font.otf", 100)
    main()
