from os import path
from mss import mss
import cv2 as cv
import numpy as np
import pydirectinput as di
import pynput.keyboard as kb
import get_window_dimensions

# HOTKEYS
STOP_KEY = 'k'
TOGGLE_KEY = 'f'
UP_KEY = 'w'
DOWN_KEY = 's'
LEFT_KEY = 'a'
RIGHT_KEY = 'd'
CONFIRM_KEY = 'enter'

def imgpath(filename):
    filename = path.join('assets', filename)
    return path.abspath(path.join(path.dirname(__file__), filename))

INDICATOR = cv.cvtColor(cv.imread(imgpath('indicator.png')), cv.COLOR_BGRA2GRAY)
UP = cv.cvtColor(cv.imread(imgpath('up.png')), cv.COLOR_BGRA2GRAY)
DOWN = cv.cvtColor(cv.imread(imgpath('down.png')), cv.COLOR_BGRA2GRAY)
LEFT = cv.cvtColor(cv.imread(imgpath('left.png')), cv.COLOR_BGRA2GRAY)
RIGHT = cv.cvtColor(cv.imread(imgpath('right.png')), cv.COLOR_BGRA2GRAY)
CIRCLE = cv.cvtColor(cv.imread(imgpath('circle.png')), cv.COLOR_BGRA2GRAY)

INDICATOR_MASK = cv.cvtColor(cv.imread(imgpath('indicator_mask.png')), cv.COLOR_BGRA2GRAY)
UP_MASK = cv.cvtColor(cv.imread(imgpath('up_mask.png')), cv.COLOR_BGRA2GRAY)
DOWN_MASK = cv.cvtColor(cv.imread(imgpath('down_mask.png')), cv.COLOR_BGRA2GRAY)
LEFT_MASK = cv.cvtColor(cv.imread(imgpath('left_mask.png')), cv.COLOR_BGRA2GRAY)
RIGHT_MASK = cv.cvtColor(cv.imread(imgpath('right_mask.png')), cv.COLOR_BGRA2GRAY)
CIRCLE_MASK = cv.cvtColor(cv.imread(imgpath('circle_mask.png')), cv.COLOR_BGRA2GRAY)

MATCH_METHOD = cv.TM_SQDIFF_NORMED

MATCH_THRESHOLD = 0.9

def matched(result):
    if (MATCH_METHOD == cv.TM_SQDIFF_NORMED):
        return cv.minMaxLoc(result)[0] < 1-MATCH_THRESHOLD
    else:
        return cv.minMaxLoc(result)[1] > MATCH_THRESHOLD

runProgram = True
runBot = False

print("With Holocure open, visit the pond and stand next to it.\n"
        f"Press {TOGGLE_KEY} to toggle bot state.")

def stop():
    print("Quit key pressed, quitting...")
    global runProgram
    runProgram = False

def toggle():
    global runBot
    runBot = not runBot
    print("Program toggled, activation status is " + str(runBot))

listener = kb.GlobalHotKeys({
    STOP_KEY: stop,
    TOGGLE_KEY: toggle
})
listener.start()

with mss() as sct:
    while (runProgram):
        if (runBot):
            window_top_left = get_window_dimensions.get_top_left("Holocure")
            INDICATOR_DIM = {"top": window_top_left[1] + 270, "left": window_top_left[0] + 1224, "width": 51, "height": 81}
            TARGET_DIM = {"top": window_top_left[1] + 726, "left": window_top_left[0] + 1143, "width": 72, "height": 63}
            indicatorSS = np.array(sct.grab(INDICATOR_DIM))
            indicatorSS = cv.cvtColor(indicatorSS, cv.COLOR_BGRA2GRAY)
            targetSS = np.array(sct.grab(TARGET_DIM))
            targetSS = cv.cvtColor(targetSS, cv.COLOR_BGRA2GRAY)

            resIndicator = cv.matchTemplate(indicatorSS, INDICATOR, MATCH_METHOD, mask=INDICATOR_MASK)

            if (matched(resIndicator)):
                print("INDICATOR MATCHED")
                resUp = cv.matchTemplate(targetSS, UP, MATCH_METHOD, mask=UP_MASK)
                resDown = cv.matchTemplate(targetSS, DOWN, MATCH_METHOD, mask=DOWN_MASK)
                resLeft = cv.matchTemplate(targetSS, LEFT, MATCH_METHOD, mask=LEFT_MASK)
                resRight = cv.matchTemplate(targetSS, RIGHT, MATCH_METHOD, mask=RIGHT_MASK)
                resCircle = cv.matchTemplate(targetSS, CIRCLE, MATCH_METHOD, mask=CIRCLE_MASK)

                if (matched(resUp)):
                    di.press(UP_KEY)
                    print("PRESSED: UP")
                elif (matched(resDown)):
                    di.press(DOWN_KEY)
                    print("PRESSED: DOWN")
                elif (matched(resLeft)):
                    di.press(LEFT_KEY)
                    print("PRESSED: LEFT")
                elif (matched(resRight)):
                    di.press(RIGHT_KEY)
                    print("PRESSED: RIGHT")
                elif (matched(resCircle)):
                    di.press(CONFIRM_KEY)
                    print("PRESSED: CONFIRM")
            else:
                di.press(CONFIRM_KEY)
                print("PRESSED: CONFIRM (ELSE)")
