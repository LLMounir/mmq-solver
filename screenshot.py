"""
Lalami Mounir
2017/11/14
Massive Music Quiz One computer
version 3.0

Fonctions de screenshots et de manipulation de fichiers image(.png)
"""

from mss import mss

sc_file = "monitor-1.png"

def screenshot():
    """ Prend un screenshot 1920/1080 du moniteur 1 """
    with mss() as sct:
        sct.shot()


if __name__ == "__main__":
    screenshot()