import ctypes
user32 = ctypes.windll.user32

SCREEN_WIDTH,SCREEN_HEIGHT = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
normal_fps = 1/60
TITLE = "Pysar0.1"
CHEMINSPRITE = "Images/C3_sprites/C3/"
