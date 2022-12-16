import sys

import pygame
from pygame.locals import BUTTON_LEFT, K_ESCAPE, K_SPACE, KEYDOWN, RESIZABLE

from data.colours import Colours
from data.game import Game
from data.metadata import MetaData

SplashScreen = False
MainMenu = False
MainGame = True
Playing = True

def diff_tuples(tuple1, tuple2):
    return tuple(map(lambda i, j: i - j, tuple1, tuple2))

def main():
    display = pygame.display.set_mode(
        (MetaData().screen_width, MetaData().screen_height), RESIZABLE
    )
    game = Game()
    game.update_player_name("James")
    game.update_lives(5)
    pygame.display.set_caption("Flappy Pong")
    background = pygame.image.load("gfx\\background.png")

    while Playing:
        td = clock.tick(60)
        td = td / 1000  # Convert milliseconds to seconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE or event.key == BUTTON_LEFT:
                    game.jump()
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.jump()

        game.update(td)
        display.fill(Colours.Black)
        display.blit(background, (0, 0))
        display.blit(game.image, game.get_position())

        current_score_text = FONT.render(str(game.score), True, (0, 0, 0))
        current_lives_text = FONT.render(str(game.lives), True, (0, 0, 0))
        display.blit(current_score_text, tuple(map(lambda i, j: i - j, (game.screen_width, game.screen_height), current_score_text.get_size())))
        display.blit(current_lives_text, (current_lives_text.get_size()[0], game.screen_height - current_lives_text.get_size()[1]))
        game.increment_score(100)
        pygame.display.update()


if __name__ == "__main__":
    clock = pygame.time.Clock()
    pygame.init()
    FONT = pygame.font.Font(pygame.font.get_default_font(), 36)
    main()
