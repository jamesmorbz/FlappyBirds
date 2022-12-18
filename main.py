import sys

import pygame
from pygame.locals import BUTTON_LEFT, K_ESCAPE, K_SPACE, KEYDOWN, RESIZABLE

from src.colours import Colours
from src.game import Game
from src.metadata import MetaData
from src.entity import Entity



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

def main():
    splash_screen = True
    MainMenu = False
    MainGame = True

    display = pygame.display.set_mode((metadata.screen_width, metadata.screen_height), RESIZABLE)

    pygame.display.set_caption("Flappy Pong")
    

    background = pygame.image.load("data\\gfx\\background.png")
    heart_image = pygame.image.load("data\\gfx\\heart.png").convert_alpha()
    heart_image = pygame.transform.scale(heart_image, (40, 40))

    logo_image = pygame.image.load("data\\gfx\\logo_image.png").convert_alpha()
    pygame.display.set_icon(logo_image)
    logo_image = pygame.transform.scale(logo_image, (200, 200))

    game = Game()
    game.update_player_name("James")
    
    entity = Entity("coin")
    mushroom = Entity("1-up")
    zoom_shoes = Entity("zoom_shoes")
    logo_text_y_coord = 30

    while True:

        if splash_screen:
            check_for_exit()
            td = clock.tick(60)
            display.fill(Colours.Black)
            display.blit(background, (0, 0))
            logo_text = pygame.image.load("data\\gfx\\logo_text.png")
            logo_text_w, logo_h = logo_text.get_size()
            logo_image_w, logo_image_h = logo_image.get_size()
            display.blit(logo_text, ((metadata.screen_width/2) - (logo_text_w/2), logo_text_y_coord))
            display.blit(logo_image, ((metadata.screen_width/2) - (logo_image_w/2), logo_text_y_coord - logo_image_h - 5))
            pygame.display.update()
            logo_text_y_coord = logo_text_y_coord + (15 / td)

            if logo_text_y_coord > metadata.screen_height:
                splash_screen = False

        if not splash_screen and not game.game_over:
            td = clock.tick(60)
            td = td / 1000  # Convert milliseconds to seconds
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

            game.update(td)
            display.fill(Colours.Black)
            display.blit(background, (0, 0))
            display.blit(game.image, game.get_position())

            display.blit(entity.sprite, (entity.coords))
            display.blit(mushroom.sprite, (mushroom.coords))
            display.blit(zoom_shoes.sprite, (zoom_shoes.coords))
            
            current_score_text = FONT.render(str(game.score), True, (0, 0, 0))

            display.blit(current_score_text, tuple(map(lambda i, j: i - j, (game.screen_width, game.screen_height), current_score_text.get_size())))
            for i in range(0, game.lives):
                x, y = heart_image.get_size()
                display.blit(heart_image, (i * x, game.screen_height - y))

            # game.increment_score(0)
            game.check_player_status()
            pygame.display.update()

        if game.game_over:
            print("Game Over")
            sys.exit(0)

if __name__ == "__main__":
    metadata = MetaData()
    pygame.init()
    clock = pygame.time.Clock()
    FONT = pygame.font.Font("data\\font\\font.otf", 36)
    main()
