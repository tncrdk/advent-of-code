import numpy as np
import time


def formatting(link: str):
    with open(link) as f:
        forest = np.asarray(f.read().split())

    return forest


def MoveNewPos(ypos, xpos):
    ypos += 1
    xpos += 3

    if xpos > 30:
        xpos = xpos - 31

    return ypos, xpos


def CheckingForTrees(ypos, xpos, forest):
    if forest[ypos][xpos] == "#":
        return True
    else:
        return False


def Navigating(link):
    forest = formatting(link)
    CountTrees = 0
    xpos = 0
    ypos = 0

    while ypos < len(forest) - 1:
        ypos, xpos = MoveNewPos(ypos, xpos)
        if CheckingForTrees(ypos, xpos, forest):
            CountTrees += 1

    return CountTrees


# =============================================================================
# Functions
# Execution
# =============================================================================

start = time.time()

link = "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\03-des\\The_Forest_Toboggan.txt"

print(Navigating(link))


print(f"Total Tid: {time.time()-start} sek")
