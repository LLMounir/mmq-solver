"""
Lalami Mounir
2017/11/14
Massive Music Quiz One computer
version 3.0

Fonctions de contrôle de la souris
"""
import time

def mouse_move(coord):
    """ Déplace la souris vers un couple de coordonnées donné """
    from pynput.mouse import Button, Controller
    mouse = Controller()
    mouse.position = (coord[0],coord[1])

def mouse_left_click():
    """ 1 clic gauche de la souris """
    from pynput.mouse import Button, Controller
    mouse = Controller()
    mouse.press(Button.left)
    mouse.release(Button.left)

def mouse_drag(start,finish):
    """ Fonction qui va effectuer un déplacement depuis start jusqu'à finish"""
    from pynput.mouse import Button, Controller
    mouse = Controller()
    mouse.position = start
    mouse.press(Button.left)
    mouse.position = finish
    time.sleep(0.1)
    mouse.position = (finish[0]+1,finish[1])
    time.sleep(0.1)
    mouse.release(Button.left)

def mouse_triple_left_click():
    """ 3 clics gauche de la souris pour sélectionner du texte facilement"""
    from pynput.mouse import Button, Controller
    mouse = Controller()
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)

if __name__ == "__main__":
    pass