import mss
import mss.tools
from PIL import Image, ImageGrab
import pytesseract
import pyautogui
import time
from tkinter import Tk

def get_pixel_colour(x, y):
    pixel = ImageGrab.grab().load()[x, y][1]
    if pixel == 3 or pixel == 0:
        return "s"
    elif pixel == 163 or pixel == 124:
        return "c"
    elif pixel == 25:
        return "d"
    elif pixel == 16:
        return "h"
    else:
        print("Something has gone wrong: " + str(ImageGrab.grab().load()[x, y]))


def interpret_message(msg):
    if "Dealing Flop" in msg:
        msg.replace("Dealer: Dealing Flop: [", "").replace("]", "")
        vals = msg.split()
        print (vals)
        global cards
        for val in vals:
            cards[convert_to_num(val) + 103] = 1

def capture(monitor, iterat):
    with mss.mss() as sct:
        img_1 = sct.grab(monitor)
        mss.tools.to_png(img_1.rgb, img_1.size,
                         output=r"C:\Users\Devin\PycharmProjects\PokerAI\Hole_Card{}.png".format(iterat))

        image = Image.open(r"C:\Users\Devin\PycharmProjects\PokerAI\Hole_Card{}.png".format(iterat))
        num = pytesseract.image_to_string(image, config='--psm 6')
        num = num.replace("‘", "").replace("I", "1")
        return num


def get_info():
    pyautogui.click(910, 1230)
    pyautogui.hotkey('ctrl', 'c')
    text = Tk().clipboard_get()
    interpret_message(text)
    time.sleep(0.1)

def convert_to_num (card):
    converter = {'Ah': 1, '2h': 2, '3h': 3, '4h': 4, '5h': 5, '6h': 6, '7h': 7, '8h': 8, '9h': 9, 'Th': 10, 'Jh': 11,
                 'Qh': 12, 'Kh': 13, 'Ac': 14, '2c': 15, '3c': 16, '4c': 17, '5c': 18, '6c': 19, '7c': 20, '8c': 21,
                 '9c': 22, 'Tc': 23, 'Jc': 24, 'Qc': 25, 'Kc': 26, 'As': 27, '2s': 28, '3s': 29, '4s': 30, '5s': 31,
                 '6s': 32, '7s': 33, '8s': 34, '9s': 35, 'Ts': 36, 'Js': 37, 'Qs': 38, 'Ks': 39, 'Ad': 40, '2d': 41,
                 '3d': 42, '4d': 43, '5d': 44, '6d': 45, '7d': 46, '8d': 47, '9d': 48, 'Td': 49, 'Jd': 50, 'Qd': 51,
                 'Kd': 52}

    return converter[card]


if __name__ == "__main__":
    cards = [0 for a in range(157)]

    #Get info for Hole Card One
    num1 = capture(monitor1, "One")
    monitor1 = {'top': 828, 'left': 1182, 'width': 28, 'height': 40}
    suit1 = get_pixel_colour(1193, 883)
    cards[convert_to_num(num1 + suit1) - 1] = 1 #Must be -1, as I started the converter dictionary from 1

    #Get info for Hole Card Two
    num2 = capture(monitor2, "Two")
    monitor2 = {'top': 828, 'left': 1287, 'width': 28, 'height': 40}
    suit2 = get_pixel_colour(1299, 883)
    cards[convert_to_num(num2 + suit2) + 51] = 1 #+51 as it's after the first 52 possible cards, but -1 for the aformentioned reason.


