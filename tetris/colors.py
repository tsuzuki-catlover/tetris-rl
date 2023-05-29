from enum import Enum


class Color(Enum):
    RED = ("Red", (255, 0, 0), "#FF0000")
    GREEN = ("Green", (0, 255, 0), "#00FF00")
    BLUE = ("Blue", (0, 0, 255), "#0000FF")
    YELLOW = ("Yellow", (255, 255, 0), "#FFFF00")
    MAGENTA = ("Magenta", (255, 0, 255), "#FF00FF")
    CYAN = ("Cyan", (0, 255, 255), "#00FFFF")
    ORANGE = ("Orange", (255, 165, 0), "#FFA500")
    PURPLE = ("Purple", (128, 0, 128), "#800080")
    PINK = ("Pink", (255, 192, 203), "#FFC0CB")
    BROWN = ("Brown", (165, 42, 42), "#A52A2A")
    GRAY = ("Gray", (128, 128, 128), "#808080")
    BLACK = ("Black", (0, 0, 0), "#000000")
    WHITE = ("White", (255, 255, 255), "#FFFFFF")
    LIGHT_BLUE = ("Light Blue", (173, 216, 230), "#ADD8E6")
    LIME_GREEN = ("Lime Green", (50, 205, 50), "#32CD32")
    GOLD = ("Gold", (255, 215, 0), "#FFD700")
    SILVER = ("Silver", (192, 192, 192), "#C0C0C0")
    NAVY_BLUE = ("Navy Blue", (0, 0, 128), "#000080")
    TEAL = ("Teal", (0, 128, 128), "#008080")
    OLIVE = ("Olive", (128, 128, 0), "#808000")

    def __init__(self, name, rgb, hex):
        self._name = name
        self._rgb = rgb
        self._hex = hex

    @property
    def name(self):
        return self._name

    @property
    def rgb(self):
        return self._rgb

    @property
    def hex(self):
        return self._hex
