"""
Lalami Mounir
2017/11/14
Massive Music Quiz One computer
version 3.0

Fonction pour trouver le bouton Try Again
"""

from PIL import Image


def find_try_again(source, try_again):
    """ Fonction qui donne les coordonnées de l'élémént try_again sur une image source donnée
    """
    im = Image.open(source)
    isize = im.size
    t_a = Image.open(try_again)
    wsize = t_a.size
    x0, y0 = wsize[0] // 2, wsize[1] // 2
    pixel = t_a.getpixel((x0, y0))[:-1]

    def diff(a, b):
        return sum((a - b) ** 2 for a, b in zip(a, b))

    best = (100000, 0, 0)
    for x in range(isize[0]):
        for y in range(isize[1]):
            ipixel = im.getpixel((x, y))
            d = diff(ipixel, pixel)
            if d < best[0]:
                best = (d, x, y)
    x, y = best[1:]

    return ((((x - x0) + (x + x0)) // 2) + 1304, y - y0)


if __name__ == "__main__":
    pass
