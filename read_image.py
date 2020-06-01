"""
Lalami Mounir
2017/11/14
Massive Music Quiz One computer
version 3.0
-------------------------------
Fonctions de contrôle du clavier
"""
import pytesseract
from PIL import Image, ImageEnhance
from screenshot import *
import time


def read_image(filename):
    """ Extraire le texte d'une image
        Return le texte
    """
    return pytesseract.image_to_string(Image.open(filename))


def crop_image(source, coord):
    """ Rogne l'image source donnée en paramètre """
    img = Image.open(source)
    area = (coord[0], coord[1], coord[2], coord[3])
    cropped_img = img.crop(area)
    cropped_img.save("assets/cropped_sc.png")


def analyze_pixel(coord):
    """ Analyse un pixel donné en coordonnée
        Et retourne un tuple de rgb
    """
    im = Image.open("monitor-1.png")  # Can be many different formats.
    pix = im.load()
    return (pix[coord[0], coord[1]])


def update_status():
    """ Analyse un screenshot et retourne une liste des différents status
    circle_status       #0=blue;1=yellow
    capture_bar_status  #0=capturing;1=found
    artist_box_status   #0=not found;1=found
    yellow_circle_color #(255, 202, 0)
    """

    artist_box = (802, 380)
    start_of_circle = (439, 265)
    capture_bar = (1753, 122)

    capture_bar_found = (255, 255, 255)
    found_color = (0, 226, 125)
    blue_circle_color = (0, 163, 243)

    time.sleep(1)
    screenshot()

    if analyze_pixel(artist_box) == found_color:
        artist_box_status = 1
    else:
        artist_box_status = 0

    if analyze_pixel(start_of_circle) == blue_circle_color:
        circle_status = 0
    else:
        circle_status = 1

    if analyze_pixel(capture_bar) == capture_bar_found:
        capture_bar_status = 1
    else:
        capture_bar_status = 0

    return [circle_status, capture_bar_status, artist_box_status]


if __name__ == "__main__":
    print("Simple: ", read_image("test.png"))
    print()
    sharp = ImageEnhance.Sharpness(Image.open("test.png"))
    sharp = sharp.enhance(0.5)
    sharp.save("test_sharpness.png")
    print("Sharpness: ", read_image("test_sharpness.png"))
    print()
    bright = ImageEnhance.Brightness(Image.open("test.png"))
    bright = bright.enhance(0.5)
    bright.save("test_brightness.png")
    print("Brightness: ", read_image("test_brightness.png"))
    print()
    contr = ImageEnhance.Contrast(Image.open("test.png"))
    contr = contr.enhance(0.5)
    contr.save("test_contrast.png")
    print("Contrast: ", read_image("test_contrast.png"))
    print()
    color = ImageEnhance.Color(Image.open("test.png"))
    color = color.enhance(0.5)
    color.save("test_color.png")
    print("Color: ", read_image("test_color.png"))