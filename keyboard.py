"""
Lalami Mounir
2017/11/15
Massive Music Quiz One computer
version 3.0

Fonctions de contrôle du clavier
NOTE: text = text.replace("\n"," ") #Tous sur une ligne pour le point bonus
"""

def tab():
    """ Effectue un tab """
    from pynput.keyboard import Key, Controller
    kb = Controller()
    kb.press(Key.tab)
    kb.release(Key.tab)


def alt_tab():
    """ Effectue un alt tab """
    from pynput.keyboard import Key, Controller
    kb = Controller()
    kb.press(Key.alt)
    kb.press(Key.tab)
    kb.release(Key.tab)
    kb.release(Key.alt)


def alt_tab_tab():
    """ Effectue deux alt tab """
    from pynput.keyboard import Key, Controller
    kb = Controller()
    kb.press(Key.alt)
    kb.press(Key.tab)
    kb.release(Key.tab)
    kb.press(Key.tab)
    kb.release(Key.tab)
    kb.release(Key.alt)


def ctrl_c():
    """ Raccourci clavier de copie"""
    from pynput.keyboard import Key, Controller
    kb = Controller()
    kb.press(Key.ctrl)
    kb.press('c')
    kb.release('c')
    kb.release(Key.ctrl)


def ctrl_v():
    """ Raccourci clavier de collage"""
    from pynput.keyboard import Key, Controller
    kb = Controller()
    kb.press(Key.ctrl)
    kb.press('v')
    kb.release('v')
    kb.release(Key.ctrl)

def ctrl_s():
    """ Raccourci clavier de sauvegarde """
    from pynput.keyboard import Key, Controller
    kb = Controller()
    kb.press(Key.ctrl)
    kb.press('s')
    kb.release('s')
    kb.release(Key.ctrl)

def clean():
    """ Raccourci clavier : efface tout ce qu'il y a dans le fichier"""
    from pynput.keyboard import Key, Controller
    kb = Controller()
    kb.press(Key.ctrl)
    kb.press('a')
    kb.release('a')
    kb.release(Key.ctrl)
    kb.press(Key.delete)
    kb.release(Key.delete)

def enter():
    """ Appui sur la touche enter du clavier"""
    from pynput.keyboard import Key, Controller
    kb = Controller()
    kb.press(Key.enter)
    kb.release(Key.enter)

def kb_type(text):
    """ Fonction qui tape au clavier le texte donné en paramètre"""
    from pynput.keyboard import Key, Controller
    kb = Controller()
    kb.type(text)

if __name__ == "__main__":
    pass

