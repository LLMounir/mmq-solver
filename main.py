"""
Lalami Mounir
2017/11/14
Massive Music Quiz One computer
version 3.0

Fichier principal
NOTE: x+1304 pour find_try_again
"""

import os
import time

from keyboard import *
from mouse import *
from read_image import *
from screenshot import *

filename_image = "assets/screenshot.png"
filename_image_source = "assets/screenshot.png"
filename_monitor = "monitor-1.png"
filename_cropped_image = "assets/cropped_sc.png"
filename_try_again_button = "assets/try_again.png"
cropping_coord = (1304,0,1920,378)

filename_text = "assets/output.txt"
filename_archive = "assets/archive.txt"

chromestesia = (1872, 70)
artist_xy = (1622, 183)
title_xy = (1626, 169)
text_xy = (1831, 109)
mmq_box = (854,297)
mmq_ok = (1276, 301)
start_of_circle = (438, 267)

circle_status = -1 #0=blue;1=yellow
capture_bar_status = -1 #0=capturing;1=found
artist_box_status = -1 #0=not found;1=found


def main():
    global capture_bar_status
    mouse_move(chromestesia)
    time.sleep(0.1)
    mouse_left_click()

    time.sleep(0.5)
    mouse_move((1767,146))
    time.sleep(0.1)
    mouse_left_click()
    while capture_bar_status != 1:
        capture_bar_status = update_status()[1]
        time.sleep(0.5)
    capture_bar_status = -1

    mouse_move(text_xy)
    mouse_triple_left_click()
    mouse_drag(text_xy,mmq_box)
    time.sleep(0.1)
    mouse_move(mmq_ok)
    mouse_left_click()

if __name__ == "__main__":
    while 1:
        main()
        while circle_status != 1:
            circle_status, capture_bar_status, artist_box_status = update_status()
            time.sleep(0.5)
        circle_status = -1
        time.sleep(6)
