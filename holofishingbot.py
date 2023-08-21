import mss.tools
import cv2 as cv
import numpy as np
import pydirectinput as di

INDICATOR = cv.imread('assets/indicator.png', cv.IMREAD_GRAYSCALE)
UP = cv.imread('assets/up.png', cv.IMREAD_GRAYSCALE)
DOWN = cv.imread('assets/down.png', cv.IMREAD_GRAYSCALE)
LEFT = cv.imread('assets/left.png', cv.IMREAD_GRAYSCALE)
RIGHT = cv.imread('assets/right.png', cv.IMREAD_GRAYSCALE)
CIRCLE = cv.imread('assets/circle.png', cv.IMREAD_GRAYSCALE)

isFishing = False

while (True):
    with mss.mss() as sct:
        indicatorDim = {"top": 270, "left": 1224, "width": 51, "height": 81}
        indicator = np.array(sct.grab(indicatorDim))
        targetDim = {"top": 708, "left": 1131, "width": 96, "height": 96}
        target = np.array(sct.grab(targetDim))

    indicator = cv.cvtColor(indicator, cv.COLOR_BGRA2GRAY)
    resIndicator = cv.matchTemplate(indicator, INDICATOR, cv.TM_CCOEFF_NORMED)

    if (cv.minMaxLoc(resIndicator)[1] > 0.9):
        isFishing = True
    else:
        isFishing = False
        di.press("e")

    if isFishing:
        target = cv.cvtColor(target, cv.COLOR_BGRA2GRAY)

        resUp = cv.matchTemplate(target, UP, cv.TM_CCOEFF_NORMED)
        resDown = cv.matchTemplate(target, DOWN, cv.TM_CCOEFF_NORMED)
        resLeft = cv.matchTemplate(target, LEFT, cv.TM_CCOEFF_NORMED)
        resRight = cv.matchTemplate(target, RIGHT, cv.TM_CCOEFF_NORMED)
        resCircle = cv.matchTemplate(target, CIRCLE, cv.TM_CCOEFF_NORMED)

        if (cv.minMaxLoc(resUp)[1] > 0.9):
            di.press("w")
        elif (cv.minMaxLoc(resDown)[1] > 0.9):
            di.press("s")
        elif (cv.minMaxLoc(resLeft)[1] > 0.9):
            di.press("a")
        elif (cv.minMaxLoc(resRight)[1] > 0.9):
            di.press("d")
        elif (cv.minMaxLoc(resCircle)[1] > 0.9):
            di.press("e")
