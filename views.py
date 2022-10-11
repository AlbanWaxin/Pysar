import time
import arcade
import arcade.gui
import globalconst as constantes
import buttons as but
import settings as sets

class MainWindow(arcade.Window):

    # intialisation de la fenetre et lancement des premières instances d'affichage
    def __init__(self):
        super().__init__(constantes.SCREEN_WIDTH, constantes.SCREEN_HEIGHT, constantes.TITLE, fullscreen=True)
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
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.logo = arcade.load_texture(constantes.CHEMINSPRITE +"C3title_00001.png")
        self.background = arcade.load_texture(constantes.CHEMINSPRITE + "0_fired_00001.png")
        arcade.set_background_color(arcade.color.AMAZON)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()
        newgame_button = but.NewGameButton(x=constantes.SCREEN_WIDTH / 2, y=constantes.SCREEN_HEIGHT/1.5 + 4*32,
                                               text="Nouvelle Partie", width=200,height=28)
        self.v_box.add(newgame_button.with_space_around(bottom=15))
        load_button = but.LoadGameButton(x=constantes.SCREEN_WIDTH / 2, y=constantes.SCREEN_HEIGHT / 1.5 + 2 * 32,
                                            text="Charger Partie", width=200, height=28)
        self.v_box.add(load_button.with_space_around(bottom=15))
        settings_button = but.SettingButton(x=constantes.SCREEN_WIDTH / 2, y=constantes.SCREEN_HEIGHT / 1.5,
                                           text="Parametres", width=200, height=28)
        self.v_box.add(settings_button.with_space_around(bottom=15))
        quit_button = but.QuitButton(x=constantes.SCREEN_WIDTH / 2, y=constantes.SCREEN_HEIGHT / 1.5 - 64,
                                            text="Quitter", width=200, height=28)
        self.v_box.add(quit_button.with_space_around(bottom=15))
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(center_x= constantes.SCREEN_WIDTH/2, center_y=constantes.SCREEN_HEIGHT/2,
                                      width=constantes.SCREEN_WIDTH, height=constantes.SCREEN_HEIGHT,
                                      texture= self.logo if self.step == 0 else self.background)
        if self.step == 1:
            for i in range(0,12):
                for j in range(0,12):
                    arcade.draw_texture_rectangle(center_x= constantes.SCREEN_WIDTH/2 + (j-5.5)*32,
                                              center_y=constantes.SCREEN_HEIGHT/1.5 + (4-i)*32,
                                              width=32, height=32,
                                              texture= arcade.load_texture(constantes.CHEMINSPRITE + "/panel/paneling_00" + str(335+i*12+j) + ".png"))
            self.manager.draw()
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.step == 0:
            self.step = 1


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