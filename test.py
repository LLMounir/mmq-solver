from pynput.mouse import Button, Controller
import time

mouse = Controller()

start = (1650,122)
finish = (1212,300)

def main():
    mouse.position = start
    mouse.press(Button.left)
    mouse.position = finish
    time.sleep(0.1)
    mouse.release(Button.left)


if __name__ == "__main__":
    main()