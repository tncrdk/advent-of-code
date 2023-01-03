import numpy as np
import time


def formatting(link: str):
    with open(link) as f:
        forest = np.asarray(f.read().split())

    return forest


def MoveNewPos1(ypos, xpos):
    ypos += 1
    xpos += 3

    if xpos > 30:
        xpos = xpos - 31

    return ypos, xpos


def MoveNewPos2(ypos, xpos):
    ypos += 1
    xpos += 1

    if xpos > 30:
        xpos = xpos - 31

    return ypos, xpos


def MoveNewPos3(ypos, xpos):
    ypos += 1
    xpos += 5

    if xpos > 30:
        xpos = xpos - 31

    return ypos, xpos


def MoveNewPos4(ypos, xpos):
    ypos += 1
    xpos += 7

    if xpos > 30:
        xpos = xpos - 31

    return ypos, xpos


def MoveNewPos5(ypos, xpos):
    ypos += 2
    xpos += 1

    if xpos > 30:
        xpos = xpos - 31

    return ypos, xpos


def CheckingForTrees(ypos, xpos, forest):
    if forest[ypos][xpos] == "#":
        return True
    else:
        return False


def Navigating1(link):
    forest = formatting(link)
    CountTrees = 0
    xpos = 0
    ypos = 0

    while ypos < len(forest) - 1:
        ypos, xpos = MoveNewPos1(ypos, xpos)
        if CheckingForTrees(ypos, xpos, forest):
            CountTrees += 1

    return CountTrees


def Navigating2(link):
    forest = formatting(link)
    CountTrees = 0
    xpos = 0
    ypos = 0

    while ypos < len(forest) - 1:
        ypos, xpos = MoveNewPos2(ypos, xpos)
        if CheckingForTrees(ypos, xpos, forest):
            CountTrees += 1

    return CountTrees


def Navigating3(link):
    forest = formatting(link)
    CountTrees = 0
    xpos = 0
    ypos = 0

    while ypos < len(forest) - 1:
        ypos, xpos = MoveNewPos3(ypos, xpos)
        if CheckingForTrees(ypos, xpos, forest):
            CountTrees += 1

    return CountTrees


def Navigating4(link):
    forest = formatting(link)
    CountTrees = 0
    xpos = 0
    ypos = 0

    while ypos < len(forest) - 1:
        ypos, xpos = MoveNewPos4(ypos, xpos)
        if CheckingForTrees(ypos, xpos, forest):
            CountTrees += 1

    return CountTrees


def Navigating5(link):
    forest = formatting(link)
    CountTrees = 0
    xpos = 0
    ypos = 0

    while ypos < len(forest) - 1:
        ypos, xpos = MoveNewPos5(ypos, xpos)
        if CheckingForTrees(ypos, xpos, forest):
            CountTrees += 1

    return CountTrees


def Combined(link):
    return (
        Navigating1(link)
        * Navigating2(link)
        * Navigating3(link)
        * Navigating4(link)
        * Navigating5(link)
    )


# =============================================================================
# Functions
# Execution
# =============================================================================

start = time.time()

link = "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\03-des\\The_Forest_Toboggan.txt"

print(Combined(link))


print(f"Total Tid: {time.time()-start} sek")
