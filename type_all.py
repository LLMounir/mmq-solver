import time
from keyboard import *
from mouse import *


mmq_ok = (1455, 307)
mmq_box = (854,297)


def main():
    f = open("assets/solution.txt",'r')
    L = f.readlines()
    f.close()

    print("Place the curser on the box and click on it.")
    time.sleep(3)

    for i in range(len(L)):
        kb_type(L[i].strip())
        time.sleep(0.2)
        mouse_move(mmq_ok)
        mouse_left_click()
        mouse_move(mmq_box)
        mouse_left_click()


if __name__ == "__main__":
    main()