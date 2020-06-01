"""
Lalami Mounir
2017/11/30
Massive Music Quiz One computer
version 4.0

Script qui va collecter tous les noms des artistes/chansons
+96
"""

import random
import os
import time

from screenshot import *
from read_image import crop_image, analyze_pixel

time_to_wait = 37

sc_file = "monitor-1.png"
soluce_xy = (350, 680, 600, 735)

soluce_folder = "/home/lalami/_/Projets/MassiveMusicQuiz/assets/soluce"

def name_generator():
    name = ""
    for i in range(12):
        name += chr(random.randint(97,122))
    return name + '.png'


def main():
    screenshot()
    crop_image(sc_file,soluce_xy)
    os.system("cp assets/cropped_sc.png assets/soluce")
    command = "mv assets/soluce/cropped_sc.png assets/soluce/" + name_generator()
    os.system(command)

if __name__ == "__main__":
    i = 0
    while 1:
        i += 1
        main()
        print("Screenshot n°{} done !".format(i))
        time.sleep(time_to_wait)
