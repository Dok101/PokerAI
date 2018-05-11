import mss
import mss.tools
from PIL import Image, ImageGrab
import pytesseract
import pyautogui
import time
from tkinter import Tk
import re

def convert_to_num (card):
    converter = {'Ah': 1, '2h': 2, '3h': 3, '4h': 4, '5h': 5, '6h': 6, '7h': 7, '8h': 8, '9h': 9, '10h': 10, 'Th': 10, 'Jh': 11,
                 'Qh': 12, 'Kh': 13, 'Ac': 14, '2c': 15, '3c': 16, '4c': 17, '5c': 18, '6c': 19, '7c': 20, '8c': 21,
                 '9c': 22, '10c': 23, 'Tc': 23, 'Jc': 24, 'Qc': 25, 'Kc': 26, 'As': 27, '2s': 28, '3s': 29, '4s': 30, '5s': 31,
                 '6s': 32, '7s': 33, '8s': 34, '9s': 35, '10s': 36, 'Ts': 36, 'Js': 37, 'Qs': 38, 'Ks': 39, 'Ad': 40, '2d': 41,
                 '3d': 42, '4d': 43, '5d': 44, '6d': 45, '7d': 46, '8d': 47, '9d': 48, '10d': 49, 'Td': 49, 'Jd': 50, 'Qd': 51,
                 'Kd': 52}

    return converter[card]

def get_pixel_colour(x, y, num):
    pixel = ImageGrab.grab().load()[x, y][1]
    if pixel == 3 or pixel == 0 or pixel == 90 or pixel == 13:
        return "s"
    elif pixel == 163 or pixel == 124 or pixel == 207 or pixel == 147:
        return "c"
    elif pixel == 25:
        return "d"
    elif pixel == 16:
        return "h"
    else:
        print("Something has gone wrong on the {} card: ".format(num) + str(ImageGrab.grab().load()[x, y]))

def interpret_message(msg):
    print (msg)
    if msg == old_msg:
        pass

    else:
        global old_msg
        global cards

        old_msg = msg

        if "Dealing Flop" in msg:
            msg = msg.replace("Dealer: Dealing Flop: [", "").replace("]", "")
            vals = msg.split()
            print (vals)
            for val in vals:
                cards[convert_to_num(val) + 103] = 1

        elif "Dealing Turn" in msg:
            msg = msg.replace("Dealer: Dealing Turn: [", "").replace("]", "")
            print (msg)
            cards[convert_to_num(msg) + 103] = 1

        elif "Dealing River" in msg:
            msg = msg.replace("Dealer: Dealing River: [", "").replace("]", "")
            print(msg)
            cards[convert_to_num(msg) + 103] = 1

        elif "raises" in msg:
            msg = msg.split("raises")[-1].split("to")[-1]
            msg = re.sub("[^0-9]", "", msg)
            print (msg)
            cards[156] = int(msg)

        elif "Starting new hand" in msg:
            global roundIsGoing
            roundIsGoing = False
            print (cards)
            init()

def capture(monitor, path, config):
    with mss.mss() as sct:
        img_1 = sct.grab(monitor)
        mss.tools.to_png(img_1.rgb, img_1.size, output=path)

        image = Image.open(path)
        num = pytesseract.image_to_string(image, config=config)
        num = num.replace("‘", "").replace("I", "1")
        return num


def get_info():
    pyautogui.click(910, 1230)
    pyautogui.hotkey('ctrl', 'c')
    text = Tk().clipboard_get()
    interpret_message(text)

def get_pot():
    global cards
    monitor = {'top': 470, 'left': 1180, 'width': 220, 'height': 50}
    cards[157] = int(capture(monitor, r"C:\Users\Devin\PycharmProjects\PokerAI\Pot_Amount.png", "--psm 7").replace("Pot: ", "").replace(",", ""))

def init ():

    roundIsGoing = True
    global cards
    cards = [0 for a in range(158)]

    # Get info for Hole Card One
    monitor1 = {'top': 828, 'left': 1182, 'width': 28, 'height': 40}
    num1 = str(capture(monitor1, r"C:\Users\Devin\PycharmProjects\PokerAI\Hole_Card_One.png", "--psm 6"))
    suit1 = get_pixel_colour(1193, 883, "1")
    cards[convert_to_num(num1 + suit1) - 1] = 1  # Must be -1, as I started the converter dictionary from 1

    # Get info for Hole Card Two
    monitor2 = {'top': 828, 'left': 1287, 'width': 28, 'height': 40}
    num2 = str(capture(monitor2, r"C:\Users\Devin\PycharmProjects\PokerAI\Hole_Card_Two.png", "--psm 6"))
    suit2 = get_pixel_colour(1299, 883, "2")
    cards[convert_to_num(num2 + suit2) + 51] = 1  #+51 as it's after the first 52 possible cards, but -1 for the aformentioned reason.

    print (str(num1) + str(suit1) + ", " + str(num2) + str(suit2))

    while roundIsGoing == True:
        for i in range (10):
            get_info()
            get_pot()
            print (cards)
if __name__ == "__main__":
    cards = []
    old_msg = ""
    init ()