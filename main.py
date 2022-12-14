import pygame
import sys
from pygame.locals import KEYDOWN, K_ESCAPE, K_SPACE, BUTTON_LEFT
from data.colours import Colours
from data.game import Game
from data.metadata import MetaData

SplashScreen = False
MainMenu = False
MainGame = True
Playing = True

def main():
    metadata = MetaData()
    display = pygame.display.set_mode((metadata.screen_width, metadata.screen_height))
    pygame.display.set_caption("Flappy Pong")
    background = pygame.image.load("gfx\\background.png")

    while Playing:
        if MainGame:
            game = Game(metadata=metadata , name = "James", difficulty = "easy")

        while Playing:
            td = clock.tick(60)
            td = td / 1000  # Convert milliseconds to seconds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE or event.key == BUTTON_LEFT:
                        game.player.jump()
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game.player.jump()

            game.player.update(td)
            display.fill(Colours.Black)
            display.blit(background, (0, 0))
            display.blit(game.player.image, game.player.get_position())

            pygame.display.update()

if __name__ == "__main__":
    clock = pygame.time.Clock()
    pygame.init()
    main()
