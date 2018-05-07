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
        return "S"
    elif pixel == 163 or pixel == 124:
        return "C"
    elif pixel == 25:
        return "D"
    elif pixel == 16:
        return "H"
    else:
        print("Something has gone wrong: " + str(ImageGrab.grab().load()[x, y]))


def interpret_message(msg):
    if msg


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
    converter = {'HA': 1, 'H2': 2, 'H3': 3, 'H4': 4, 'H5': 5, 'H6': 6, 'H7': 7, 'H8': 8, 'H9': 9, 'HT': 10, 'HJ': 11,
                 'HQ': 12, 'HK': 13, 'CA': 14, 'C2': 15, 'C3': 16, 'C4': 17, 'C5': 18, 'C6': 19, 'C7': 20, 'C8': 21,
                 'C9': 22, 'CT': 23, 'CJ': 24, 'CQ': 25, 'CK': 26, 'SA': 27, 'S2': 28, 'S3': 29, 'S4': 30, 'S5': 31,
                 'S6': 32, 'S7': 33, 'S8': 34, 'S9': 35, 'ST': 36, 'SJ': 37, 'SQ': 38, 'SK': 39, 'DA': 40, 'D2': 41,
                 'D3': 42, 'D4': 43, 'D5': 44, 'D6': 45, 'D7': 46, 'D8': 47, 'D9': 48, 'DT': 49, 'DJ': 50, 'DQ': 51,
                 'DK': 52}


if __name__ == "__main__":
    cards = [0 for a in range(367)]

    #Get info for Hole Card One
    num1 = capture(monitor1, "One")
    monitor1 = {'top': 828, 'left': 1182, 'width': 28, 'height': 40}
    suit1 = get_pixel_colour(1193, 883)
    cards[convert_to_num(suit1 + num1)] = 1

    #Get info for Hole Card Two
    num2 = capture(monitor2, "Two")
    monitor2 = {'top': 828, 'left': 1287, 'width': 28, 'height': 40}
    suit2 = get_pixel_colour(1299, 883)
    cards[convert_to_num(suit2 + num2)] = 1
