def Formatting(link):
    with open(link) as f:
        txt = f.read().split()
        txt = [int(i) for i in txt]

    return txt


def FindingFirstOut(Numberslist: list):
    for i in range(25, len(Numberslist)):
        Valid = False
        for x in range(i - 25, i - 1):
            if Numberslist[i] - Numberslist[x] in Numberslist[i - 25 : i]:
                Valid = True
                break

        if not Valid:
            print(Numberslist[i])
            return i


# =============================================================================
# Functions
# Execution
# =============================================================================

link = "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\09-des\\PreAmbles.txt"

Numberslist = Formatting(link)

FindingFirstOut(Numberslist)
