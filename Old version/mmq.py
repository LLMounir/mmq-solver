"""
Lalami Mounir
2017/11/14
Massive Music Quiz One computer 
version 3.0
NOTE : 25x zoom pour setup
"""
#Image to text
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
#Type Out
import os
import uinput
import subprocess
import time
from mss import mss
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller


filename_text = "output.txt"
filename_image = "screenshot.png"
archive = "archive.txt"
source_image = "/home/lalami/monitor-1.png"

def main(filename_image, filename_text):
    """ Prend le nom des fichiers en paramètre
        Appel les autres fonctions dans le bonne ordre
        #TODO: Implémenter sys.argv[]
        Ne renvoie rien
    """
    aha = (1870, 71)
    mmq_tab = (302, 36)
    mmq_box = (854,297)
    other_tab = (87, 38)
    artist_xy = (1622, 183)
    title_xy = (1626, 169)
   
    #Setup
    input("Press any key to continue...")
    print("Work in progress...")
    mouse_move_pynput(aha[0],aha[1])
    mouse_left_click()
    time.sleep(3)
    input("Press any key to continue...")
    print("Work in progress...\o.o/")
    mouse_move_pynput(other_tab[0],other_tab[1])
    mouse_left_click()
    mouse_move_pynput(aha[0],aha[1])
    mouse_left_click()
    time.sleep(3)
    mouse_move_pynput(artist_xy[0],artist_xy[1])
    time.sleep(1)
    mouse_triple_left_click()
    time.sleep(1)
    ctrl_c()
    time.sleep(1)
    alt_tab_tab()
    time.sleep(1)
    enter(),enter(),enter()
    time.sleep(1)
    tab(),tab()
    time.sleep(1)
    ctrl_v()
    time.sleep(1)
    enter()
    time.sleep(1)
    tab(),tab()
    time.sleep(1)
    alt_tab()
    time.sleep(1)
    mouse_move_pynput(aha[0],aha[1])
    time.sleep(1)
    mouse_left_click()
    time.sleep(1)
    time.sleep(3)
    time.sleep(1)
    mouse_move_pynput(title_xy[0],title_xy[1])
    time.sleep(1)
    mouse_triple_left_click()
    time.sleep(1)
    ctrl_c()
    time.sleep(1)
    alt_tab()
    time.sleep(1)
    ctrl_v()
    time.sleep(1)
    enter(),enter(),enter(),enter()
    time.sleep(1)
    screenshot()
    time.sleep(1)
    clean()
    time.sleep(1)
    alt_tab()
    time.sleep(1)
    mouse_move_pynput(mmq_tab[0],mmq_tab[1])
    time.sleep(1)
    mouse_left_click()
    time.sleep(1)
    mouse_move_pynput(mmq_box[0],mmq_box[1])
    time.sleep(1)
    mouse_left_click()
    time.sleep(1)
    
    #Image to text
    crop_image(source_image)
    text = read_image(filename_image)            
    write_output(filename_text,text)
    write_archive(archive,text)
     
    f = open(filename_text,'r')
    artist = f.read().strip()
    title = f.read().strip()
    f.close()
    
    text = artist + " " + title
    
    text = text.replace("\n"," ") #Tous sur une ligne pour le point bonus
    
    for ch in text:
        subprocess.call(["xdotool", "type", ch])
        #time.sleep(0.01)
        #TODO: Latences ?


def crop_image(source):
    """ Rogne la capture d'écran de la fenêtre shazam
    """
    img = Image.open(source)
    area = (472, 203,1677, 423)
    cropped_img = img.crop(area)
    cropped_img.save("screenshot.png")

def screenshot():
    """ Prend un screenshot de l'écran complet
    """
    with mss() as sct:
        sct.shot()
    print("screenshot done !")
    
def read_image(filename):
    """ Extraie le texte de l'image
        Retourne le texte
    """
    #TODO: Vérifier si l'extension influence les résultats
    #TODO: Offrir un choix multiple à l'utilisateur
    #TODO: Une option?
    
    return pytesseract.image_to_string(Image.open(filename))

def write_output(filename,text):
    """ Ecris le texte extraie dans le fichier de sortie
    """
    f = open(filename,"w")
    f.write(text)
    f.close()

def tab():
    from pynput.keyboard import Key, Controller
    """ Effectue un tab
    """
    kb = Controller()
    kb.press(Key.tab)
    kb.release(Key.tab)
        
def alt_tab():
    from pynput.keyboard import Key, Controller
    """ Effectue un alt tab
    """
    kb = Controller()
    kb.press(Key.alt)
    kb.press(Key.tab)
    kb.release(Key.tab)
    kb.release(Key.alt)

def alt_tab_tab():
    from pynput.keyboard import Key, Controller
    """ Effectue deux alt tab
    """
    kb = Controller()
    kb.press(Key.alt)
    kb.press(Key.tab)
    kb.release(Key.tab)
    kb.press(Key.tab)
    kb.release(Key.tab)
    kb.release(Key.alt)

def ctrl_c():
    from pynput.keyboard import Key, Controller
    kb = Controller()
    kb.press(Key.ctrl)
    kb.press('c')
    kb.release('c')
    kb.release(Key.ctrl)

def ctrl_v():
    from pynput.keyboard import Key, Controller
    kb = Controller()
    kb.press(Key.ctrl)
    kb.press('v')
    kb.release('v')
    kb.release(Key.ctrl)

def clean():
    from pynput.keyboard import Key, Controller
    kb = Controller()
    kb.press(Key.ctrl)
    kb.press('a')
    kb.release('a')
    kb.release(Key.ctrl)
    kb.press(Key.delete)
    kb.release(Key.delete)

def enter():
    from pynput.keyboard import Key, Controller
    kb = Controller()
    kb.press(Key.enter)
    kb.release(Key.enter)

def write_archive(filename,text):
    f = open(filename,"a")
    f.write(text)
    f.write("\n")
    f.write("--------------------------")
    f.write("\n")
    f.close()

def mouse_move_pynput(x,y):
    from pynput.mouse import Button, Controller
    """ Déplace la souris vers un couple de coordonnées donné
    """
    mouse = Controller()
    mouse.position = (x,y)

def mouse_left_click():
    from pynput.mouse import Button, Controller
    """ 1 clic gauche de la souris
    """
    mouse = Controller()
    mouse.press(Button.left)
    mouse.release(Button.left)

def mouse_triple_left_click():
    from pynput.mouse import Button, Controller
    """ 3 clics gauche de la souris
    """
    mouse = Controller()
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)

def mouse_move_uinput():
    """ Prends le relai si la souris se trouve sur un autre écran
        pour la ramener sur le monitor1
    """
    events = (
        uinput.REL_X,
        uinput.REL_Y,
        uinput.BTN_LEFT,
        uinput.BTN_RIGHT,
        )

    with uinput.Device(events) as device:
        for i in range(20):
            # syn=False
            device.emit(uinput.REL_X, 5, syn=False)
            device.emit(uinput.REL_Y, 5)
            time.sleep(0)


if __name__ == "__main__":
    main(filename_image,filename_text)