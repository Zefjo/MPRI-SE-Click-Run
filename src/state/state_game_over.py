from state_engine import GameState
import pygame as pg


class GameOver(GameState):
    """
    The state for the game over.
    """
    def __init__(self) -> None:
        GameState.__init__(self)

    def get_event(self, event: pg.event) -> None:
        """
        Do something according to the last event that happened.
        @param event: the last event that occurred.
        """
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.next_state = "MAIN_MENU"
                self.restart_next_state = False
                self.done = True

            elif event.key == pg.K_RETURN:
                self.next_state = "GAME"
                self.restart_next_state = True
                self.done = True

    def draw(self, surface: pg.Surface) -> None:
        """
        Draw everything to the screen.
        @param surface: The surface that will be displayed.
        """
        width, height = surface.get_size()

        surface.fill(pg.Color("black"))
        text_color = 255, 255, 255

        text = self.font.render("GAME_OVER", 1, text_color)
        width_text, height_text = text.get_size()
        surface.blit(text, ((width - width_text) / 2, (height - height_text) / 2))

        text = self.font.render("Press enter if you want to start a new game\n", 1, text_color)
        width_text, height_text = text.get_size()
        surface.blit(text, ((width - width_text) / 2, (height - height_text) / 2 + 24))

        text = self.font.render("Press escape if you want to go back to the main menu\n", 1, text_color)
        width_text, height_text = text.get_size()
        surface.blit(text, ((width - width_text) / 2, (height - height_text) / 2 + 48))

        pg.display.flip()
