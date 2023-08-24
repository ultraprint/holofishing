import mss.tools
import cv2 as cv
import numpy as np
import pydirectinput as di

UP_KEY = 'w'
DOWN_KEY = 's'
LEFT_KEY = 'a'
RIGHT_KEY = 'd'
CONFIRM_KEY = 'e'

INDICATOR = cv.cvtColor(cv.imread('assets/indicator.png'), cv.COLOR_BGRA2GRAY)
UP = cv.cvtColor(cv.imread('assets/up.png'), cv.COLOR_BGRA2GRAY)
DOWN = cv.cvtColor(cv.imread('assets/down.png'), cv.COLOR_BGRA2GRAY)
LEFT = cv.cvtColor(cv.imread('assets/left.png'), cv.COLOR_BGRA2GRAY)
RIGHT = cv.cvtColor(cv.imread('assets/right.png'), cv.COLOR_BGRA2GRAY)
CIRCLE = cv.cvtColor(cv.imread('assets/circle.png'), cv.COLOR_BGRA2GRAY)

INDICATOR_MASK = cv.cvtColor(cv.imread('assets/indicator_mask.png'), cv.COLOR_BGRA2GRAY)
UP_MASK = cv.cvtColor(cv.imread('assets/up_mask.png'), cv.COLOR_BGRA2GRAY)
DOWN_MASK = cv.cvtColor(cv.imread('assets/down_mask.png'), cv.COLOR_BGRA2GRAY)
LEFT_MASK = cv.cvtColor(cv.imread('assets/left_mask.png'), cv.COLOR_BGRA2GRAY)
RIGHT_MASK = cv.cvtColor(cv.imread('assets/right_mask.png'), cv.COLOR_BGRA2GRAY)
CIRCLE_MASK = cv.cvtColor(cv.imread('assets/circle_mask.png'), cv.COLOR_BGRA2GRAY)

MATCH_METHOD = cv.TM_SQDIFF_NORMED
MATCH_THRESHOLD = 0.9

def matched(result):
    if (MATCH_METHOD == cv.TM_SQDIFF_NORMED):
        return cv.minMaxLoc(result)[0] < 1-MATCH_THRESHOLD
    else:
        return cv.minMaxLoc(result)[1] > MATCH_THRESHOLD

while (True):
    with mss.mss() as sct:
        indicatorDim = {"top": 270, "left": 1224, "width": 51, "height": 81}
        indicatorSS = np.array(sct.grab(indicatorDim))
        indicatorSS = cv.cvtColor(indicatorSS, cv.COLOR_BGRA2GRAY)
        targetDim = {"top": 726, "left": 1143, "width": 72, "height": 63}
        targetSS = np.array(sct.grab(targetDim))
        targetSS = cv.cvtColor(targetSS, cv.COLOR_BGRA2GRAY)

    resIndicator = cv.matchTemplate(indicatorSS, INDICATOR, MATCH_METHOD, mask=INDICATOR_MASK)

    if (matched(resIndicator)):
        resUp = cv.matchTemplate(targetSS, UP, MATCH_METHOD, mask=UP_MASK)
        resDown = cv.matchTemplate(targetSS, DOWN, MATCH_METHOD, mask=DOWN_MASK)
        resLeft = cv.matchTemplate(targetSS, LEFT, MATCH_METHOD, mask=LEFT_MASK)
        resRight = cv.matchTemplate(targetSS, RIGHT, MATCH_METHOD, mask=RIGHT_MASK)
        resCircle = cv.matchTemplate(targetSS, CIRCLE, MATCH_METHOD, mask=CIRCLE_MASK)

        if (matched(resUp)):
            di.press(UP_KEY)
        elif (matched(resDown)):
            di.press(DOWN_KEY)
        elif (matched(resLeft)):
            di.press(LEFT_KEY)
        elif (matched(resRight)):
            di.press(RIGHT_KEY)
        elif (matched(resCircle)):
            di.press(CONFIRM_KEY)
    else:
        di.press(CONFIRM_KEY)
