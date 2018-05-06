import mss
import mss.tools
from PIL import Image, ImageGrab
import pytesseract
import numpy as np


# def classify (avg_colour):
# Diamonds = (9, 9, 237) =
# Spades = (0, 0, 0) =
# Hearts = (201, 16, 16) =
# Clubs = (57. 140, 27) =

def get_pixel_colour(x, y):
    pixel = ImageGrab.grab().load()[x, y][1]
    if pixel == 3 or pixel == 0:
        return "S"
    elif pixel == 163 or pixel == 124:
        return "C"
    elif pixel == 25:
        return "D"
    elif pixel == 16:
        return "H"
    else:
        print("Something has gone wrong: " + str(ImageGrab.grab().load()[x, y]))


def capture(monitor, iterat):
    with mss.mss() as sct:
        img_1 = sct.grab(monitor)
        mss.tools.to_png(img_1.rgb, img_1.size,
                         output=r"C:\Users\Devin\PycharmProjects\PokerAI\Hole_Card{}.png".format(iterat))

        image = Image.open(r"C:\Users\Devin\PycharmProjects\PokerAI\Hole_Card{}.png".format(iterat))
        num = pytesseract.image_to_string(image, config='--psm 6')
        num = num.replace("'", "")
        return num


if __name__ == "__main__":
    monitor1 = {'top': 828, 'left': 1182, 'width': 28, 'height': 40}
    monitor2 = {'top': 828, 'left': 1287, 'width': 28, 'height': 40}

    num1 = capture(monitor1, "One")
    num2 = capture(monitor2, "Two")

    suit1 = get_pixel_colour(1193, 883)
    suit2 = get_pixel_colour(1299, 883)

    print(str(num1) + suit1)
    print(str(num2) + suit2)
