"""
This is a script that draws an image of a town
"""
import arcade
import random
#Constants
SCREEN_WIDTH= 900
SCREEN_HEIGHT= 700
TITLE= "Drawing Test"
FIRST_SECTION_HEIGHT = 200


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
        self.set_update_rate(1)
        self.colors_list = None
        self.stars = []

    def setup(self):
        self.colors_list = [arcade.color.CARMINE_PINK,arcade.color.CANDY_PINK,arcade.color.BITTERSWEET,
                           arcade.color.DEEP_CHAMPAGNE, arcade.color.BLACK]
        self.stars = [(0, 0, arcade.color.WHITE) for k in range(10)]

    def on_draw(self):
        #Draw all backgrounds
        frst_sect_y = SCREEN_HEIGHT - FIRST_SECTION_HEIGHT
        oth_sect_height= frst_sect_y/5

        arcade.draw_lrtb_rectangle_filled(0,SCREEN_WIDTH,SCREEN_HEIGHT, frst_sect_y,
                                          arcade.color.CARMINE_RED)
        for i in range(5):
            arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, frst_sect_y, frst_sect_y-oth_sect_height,
                                              self.colors_list[i])
            frst_sect_y -= oth_sect_height

        for k in self.stars:
            (x, y, c) = k
            arcade.draw_rectangle_filled(x, y, 5, 5, c)

    def on_update(self, delta_time: float):
        self.set_update_rate(delta_time-(delta_time/10))
        for i in range(len(self.stars)):
            if i % 2 == 0:
                color= arcade.color.WHITE
            else:
                color = arcade.color.VIOLET
            x = random.randrange(5, SCREEN_WIDTH - 5)
            y = random.randrange(SCREEN_HEIGHT - FIRST_SECTION_HEIGHT + 5, SCREEN_HEIGHT - 5)
            self.stars[i] = (x, y, color)
        print(self.get_viewport())

    def on_hide(self):
        print("cache")

def main():
    window = MyGame()
    window.setup()
    arcade.enable_timings(100)

    arcade.run()

main()