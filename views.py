import time
import arcade
import globalconst as constantes
import settings as sets

class MainWindow(arcade.Window):

    # intialisation de la fenetre et lancement des premières instances d'affichage
    def __init__(self):
        super().__init__(constantes.SCREEN_WIDTH, constantes.SCREEN_HEIGHT, constantes.TITLE)
        self.set_update_rate(constantes.normal_fps)

        # Différents écrans:
        self.welcomescreen = WelcomeScreen()
        self.settingscreen = SettingScreen()
        self.loadscreen = LoadScreen()
        self.gamescreen = Game()

    # Lancement
    def setup(self):
        self.show_view(self.welcomescreen)

    # Comportement en cas de minimisation de la fenetre
    def on_hide(self):
        self.set_update_rate(0)

    def on_show(self):
        self.set_update_rate(constantes.normal_fps)

    # Fonctions d'acquisition d'action joueur
    # Deplacement de la souris dans la fenetre
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        pass
    # Roulement mollette (affectiation du zoom ou lecture texte
    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        pass

    # Click de Souris
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        pass

    #Appuies de Touches
    def on_key_press(self, symbol: int, modifiers: int):
        match symbol:
            case _: pass

class WelcomeScreen(arcade.View):

    def __init__(self):
        super().__init__()
        self.step = 0
        #self.background = arcade.load_texture("logo.png")
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()
        pass


class Game(arcade.View):

    def __init__(self):
        self.window: MainWindow
        super().__init__()

class SettingScreen(arcade.View):
    pass

class LoadScreen(arcade.View):
    pass

def main():
    window = MainWindow()
    window.setup()
    arcade.run()