import mss
import mss.tools
import uuid
import time

if __name__ == "__main__":
    with mss.mss() as sct:
        monitor1 = {'top':828, 'left':1180, 'width':30, 'height':72}
        monitor2 = {'top':828, 'left':1285, 'width':30, 'height':72}
        monitor3 = {'top':540, 'left':1005, 'width':30, 'height':72}
        monitor4 = {'top':540, 'left':1119, 'width':30, 'height':72}
        monitor5 = {'top':540, 'left':1233, 'width':30, 'height':72}
        monitor6 = {'top':540, 'left':1347, 'width':30, 'height':72}
        monitor7 = {'top':540, 'left':1461, 'width':30, 'height':72}

        for i in range (508, 10000):
            sct_1 = sct.grab(monitor1)
            sct_2 = sct.grab(monitor2)
            sct_3 = sct.grab(monitor3)
            sct_4 = sct.grab(monitor4)
            sct_5 = sct.grab(monitor5)
            sct_6 = sct.grab(monitor6)
            sct_7 = sct.grab(monitor7)

            mss.tools.to_png(sct_1.rgb, sct_1.size, output='C:/Users/Devin/Desktop/PokerBot/CardsImages/Hole_Card_{}.png'.format(i*7-7))
            mss.tools.to_png(sct_2.rgb, sct_2.size, output='C:/Users/Devin/Desktop/PokerBot/CardsImages/Hole_Card_{}.png'.format(i*7-6))
            mss.tools.to_png(sct_3.rgb, sct_3.size, output='C:/Users/Devin/Desktop/PokerBot/CardsImages/Hole_Card_{}.png'.format(i*7-5))
            mss.tools.to_png(sct_4.rgb, sct_4.size, output='C:/Users/Devin/Desktop/PokerBot/CardsImages/Hole_Card_{}.png'.format(i*7-4))
            mss.tools.to_png(sct_5.rgb, sct_5.size, output='C:/Users/Devin/Desktop/PokerBot/CardsImages/Hole_Card_{}.png'.format(i*7-3))
            mss.tools.to_png(sct_6.rgb, sct_6.size, output='C:/Users/Devin/Desktop/PokerBot/CardsImages/Hole_Card_{}.png'.format(i*7-2))
            mss.tools.to_png(sct_7.rgb, sct_7.size, output='C:/Users/Devin/Desktop/PokerBot/CardsImages/Hole_Card_{}.png'.format(i*7-1))
            print ("Taking screenshots")            
            time.sleep(20)
