import sys

import logging
import pygame
from pygame.locals import K_ESCAPE, K_SPACE, KEYDOWN, RESIZABLE

from src.colours import Colours
from src.game import Game
from src.metadata import MetaData
from src.button import Button
import src.helper as helper

def main():
    helper.default_config_creation()
    config = helper.read_config()
    splash_screen = config.get("load_with_splash_screen", True)
    background_colour = tuple(config.get("background_colour", (81, 159, 204)))
    game_over_colour = tuple(config.get("game_over_colour", (200, 95, 255)))
    last_played_user = config.get("last_played_user", None)
    main_menu = True

    display = pygame.display.set_mode((metadata.screen_size), RESIZABLE)

    pygame.display.set_caption("Flappy Pong")

    game = Game()
    pygame.display.set_icon(game.logo_image)
    logo_text_y_coord = 30
    
    start_button = Button(Colours.Green, 100,300,150,100, "Start", SMALL_FONT)
    quit_button = Button(Colours.Red, metadata.screen_width-90,0,90,50, "Quit", SMALL_FONT)
    options_button = Button(Colours.LightGreen, 390,300,150,100, "Options", SMALL_FONT)
    text_input = Button(Colours.Blue, 120,150,400,50, " ", SMALL_FONT)
    play_again_button = Button(Colours.Maroon, 170,120,300,200, "PLAY AGAIN", SMALL_FONT)
    if last_played_user is not None:
        username = last_played_user
    else:
        username = "ENTER NAME"
    active_typing = False
    current_highscore = helper.get_current_highscore()

    while True:
        if splash_screen:
            td = clock.tick(60)
            display.fill(background_colour)
            logo_text = pygame.image.load("data\gfx\logo_text.png")
            logo_text_w, logo_h = logo_text.get_size()
            logo_image_w, logo_image_h = game.logo_image.get_size()
            display.blit(logo_text,((metadata.screen_width / 2) - (logo_text_w / 2), logo_text_y_coord))
            display.blit(game.logo_image,((metadata.screen_width / 2) - (logo_image_w / 2),logo_text_y_coord - logo_image_h - 5,))
            logo_text_y_coord = logo_text_y_coord + (15 / td)

            if logo_text_y_coord > metadata.screen_height:
                splash_screen = False
                
                td = clock.tick(60)

            helper.check_for_exit()

        elif main_menu:
            td = clock.tick(60)
            display.fill(background_colour)
            
            start_button.draw(display)
            quit_button.draw(display)
            options_button.draw(display)
            text_input.draw(display)
            username_text = SMALL_FONT.render(username, True, Colours.White)
            display.blit(username_text, (130,155))

            current_highscore_text = TINY_FONT.render(current_highscore, True, Colours.Black)
            display.blit(current_highscore_text, (0,0))

            if any(pygame.mouse.get_pressed()):
                if start_button.hover():
                    if username != "ENTER NAME" and username:
                        main_menu = False
                        helper.write_config({"last_played_user": username})
                        td = clock.tick(60)

                if quit_button.hover():
                    helper.exit_game()

                if options_button.hover():
                    logging.info("NOT IMPLEMENTED YET!")

                if text_input.hover():
                    active_typing = True
                    username = ""
                else:
                    active_typing = False
            
            if active_typing:
                text_input.color = Colours.LightBlue
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            username = username[:-1]
                        else:
                            username += event.unicode
                            game.update_player_name(username)
            else:
               text_input.color = Colours.Blue

            helper.check_for_exit()
            
        elif not game.game_over:
            td = clock.tick(60)
            td = td / 1000  # Convert milliseconds to seconds

            display.fill(background_colour)

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

            display.blit(current_score_text, helper.diff_tuples(game.screen_size,current_score_text.get_size()))
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
                x, y = game.heart_image.get_size()
                display.blit(game.heart_image, (i * x, game.screen_height - y))

        elif game.game_over:
            display.fill(game_over_colour)
            game_over = SMALL_FONT.render(f"GAME OVER {game.name}. You Scored {game.score}", True, Colours.White)
            display.blit(game_over, helper.diff_tuples(game.screen_size, game_over.get_size()))
            play_again_button.draw(display)
            quit_button.draw(display)

            if any(pygame.mouse.get_pressed()):
                if play_again_button.hover():
                    game = Game(name=game.name)
                    current_highscore = helper.get_current_highscore()
                    main_menu = True
                    td = clock.tick(60)
                if quit_button.hover():
                    helper.exit_game()

            game.write_to_scoreboard()
            helper.check_for_exit()

        pygame.display.update()
        

if __name__ == "__main__":
    metadata = MetaData()
    pygame.init()
    clock = pygame.time.Clock()
    TINY_FONT = pygame.font.Font("data\\font\\font.otf", 16)
    SMALL_FONT = pygame.font.Font("data\\font\\font.otf", 36)
    BIG_FONT = pygame.font.Font("data\\font\\font.otf", 100)
    main()
