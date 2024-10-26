from pyautogui import  click, locateCenterOnScreen, sleep, middleClick, hotkey


from pynput.keyboard import KeyCode, Key, Controller

import time


def s(seconds):
    # print("taking a nap")
    return sleep(seconds)


def c(*args, **kwargs):
    return click(*args, **kwargs, interval=0.55)

  

def rp():
    # reset position click random spot
    c(x=1316, y=448)


def img(i):
    while True:
        try:
            return locateCenterOnScreen(f"images/{i}.png", confidence=.98)
        except:
            # print("image not found try again in 1 second")
            s(2)


def click_img(i):
    x, y = img(i)
    c(x=x, y=y)

    

    
def check_if_collection_event_is_on_screen():
    try:
        s(3)
        x, y = locateCenterOnScreen(f"images/collect.png", confidence=.98)
        print("wow collect very cool")
        c(x=x, y=y)
        s(1)
        c(x=1524, y=735)
        c(x=1278, y=735)
        s(1)
        c(x=1272, y=735)
        c(x=1272, y=735)
        s(1)
        c(x=1030, y=735)
        c(x=1272, y=735)
        s(1)
        c(x=1405, y=735)
        c(x=1272, y=735)
        s(1)
        c(x=1151, y=735)
        c(x=1272, y=735)
        s(1)
        c(x=1030, y=1112)
        c(x=543, y=321)
       
    except:
        pass
   



def navigate_to_ouch():    
    s(1)
    c(x=1183, y=1095)
    c(x=719, y=675)
    c(x=1642, y=796)
    c(x=1570, y=679)
    c(x=1555, y=943)
    s (5)
    c(x=1294, y=946)
def play_the_game():
    s(1)
    click_img("monkey_buccaneer")
    c(x=1274, y=720)


    img("round_6")
    c(x=2000, y=944)
    c(x=1190, y=778)
    c(x=2000, y=944)
    c(x=1106, y=721)

    
    c(x=1274, y=720)
    c(x=755, y=684, clicks=6)
    c(x=1106, y=721)
    c(x=759, y=941, clicks=6)
    c(x=1190, y=778)
    c(x=763, y=813, clicks=6)
    c(x=1423, y=1000)

   
    hotkey('fn', 'f8')
    
    keyboard = Controller()
    s(0.5)
    c (x=1282, y=746)
    s(0.5)
    keyboard.press('9')
    keyboard.release('9')
    s(0.5)
    keyboard.press('9')
    keyboard.release('9')
    s(0.5)
    c (x=1430, y=840)





    c(x=2005, y=1118)
    c(x=2000, y=1125)




    img("instamonkey")
    s(0.2)
    rp()
    


    img("next")
    s(0.2)
    c(x=1283, y=1035)




    img("home")
    s(0.2)
    c(x=1079, y=990)


  


    



def main():
    print("starting in 7 seconds")
    print("click game window before the script starts")
    print("press ctrl+c to exit")
    try:
        s(5)
        while True:
            s(1.5)
            check_if_collection_event_is_on_screen()
            navigate_to_dark_castle()
            play_the_game()
    except KeyboardInterrupt:
        print("exiting...")


if __name__ == "__main__":
    main()

print("This line will be executed")
