import mss.tools
import cv2 as cv
import numpy as np
import pydirectinput as di

UP_KEY = 'w'
DOWN_KEY = 's'
LEFT_KEY = 'a'
RIGHT_KEY = 'd'
CONFIRM_KEY = 'e'

INDICATOR = cv.imread('assets/indicator.png', cv.IMREAD_GRAYSCALE)
UP = cv.imread('assets/up.png', cv.IMREAD_GRAYSCALE)
DOWN = cv.imread('assets/down.png', cv.IMREAD_GRAYSCALE)
LEFT = cv.imread('assets/left.png', cv.IMREAD_GRAYSCALE)
RIGHT = cv.imread('assets/right.png', cv.IMREAD_GRAYSCALE)
CIRCLE = cv.imread('assets/circle.png', cv.IMREAD_GRAYSCALE)

MATCH_METHOD = cv.TM_CCOEFF_NORMED

isFishing = False

while (True):
    with mss.mss() as sct:
        indicatorDim = {"top": 270, "left": 1224, "width": 51, "height": 81}
        indicator = np.array(sct.grab(indicatorDim))
        targetDim = {"top": 726, "left": 1131, "width": 96, "height": 63}
        target = np.array(sct.grab(targetDim))

    indicator = cv.cvtColor(indicator, cv.COLOR_BGRA2GRAY)
    resIndicator = cv.matchTemplate(indicator, INDICATOR, MATCH_METHOD)

    if (cv.minMaxLoc(resIndicator)[1] > 0.9):
        isFishing = True
    else:
        isFishing = False
        di.press(CONFIRM_KEY)

    if isFishing:
        target = cv.cvtColor(target, cv.COLOR_BGRA2GRAY)

        resUp = cv.matchTemplate(target, UP, MATCH_METHOD)
        resDown = cv.matchTemplate(target, DOWN, MATCH_METHOD)
        resLeft = cv.matchTemplate(target, LEFT, MATCH_METHOD)
        resRight = cv.matchTemplate(target, RIGHT, MATCH_METHOD)
        resCircle = cv.matchTemplate(target, CIRCLE, MATCH_METHOD)

        if (cv.minMaxLoc(resUp)[1] > 0.9):
            di.press(UP_KEY)
        elif (cv.minMaxLoc(resDown)[1] > 0.9):
            di.press(DOWN_KEY)
        elif (cv.minMaxLoc(resLeft)[1] > 0.9):
            di.press(LEFT_KEY)
        elif (cv.minMaxLoc(resRight)[1] > 0.9):
            di.press(RIGHT_KEY)
        elif (cv.minMaxLoc(resCircle)[1] > 0.9):
            di.press(CONFIRM_KEY)
