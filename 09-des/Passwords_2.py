def Formatting(link):
    with open(link) as f:
        txt = f.read().split()
        txt = [int(i) for i in txt]

    return txt


def FindContigousNumbers(Numberslist: list, Target):
    for i in range(len(Numberslist)):
        if Numberslist[i] != Target:
            Sum = 0
            elements = 1
            while Sum < Target:
                Sum = sum(Numberslist[i : i + elements])
                if Sum == Target:
                    Sol = [x for x in Numberslist[i : i + elements]]
                    print(min(Sol) + max(Sol))
                    return

                elements += 1


# =============================================================================
# Functions
# Execution
# =============================================================================

link = "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\09-des\\PreAmbles.txt"

Target = 25918798

Numberslist = Formatting(link)

FindContigousNumbers(Numberslist, Target)
