def Formatting(link):
    with open(link) as f:
        txt = f.read().split("\n")

    txt = [[i.split()[0], int(i.split()[1])] for i in txt]

    return txt


def CheckForError(Instructions: list):
    AlreadyDone = set()
    acc = 0
    Index = 0

    while Index < len(Instructions):
        if Index in AlreadyDone:
            return False

        if Instructions[Index][0] == "acc":
            AlreadyDone.add(Index)
            acc += Instructions[Index][1]
            Index += 1
        elif Instructions[Index][0] == "jmp":
            AlreadyDone.add(Index)
            Index += Instructions[Index][1]
        elif Instructions[Index][0] == "nop":
            AlreadyDone.add(Index)
            Index += 1

    print(acc)
    return True


def FixError(Instructions: list):
    for i in Instructions:
        if i[0] == "jmp":
            i[0] = "nop"
            if CheckForError(Instructions):
                return
            else:
                i[0] = "jmp"

        if i[0] == "nop":
            i[0] = "jmp"
            if CheckForError(Instructions):
                return
            else:
                i[0] = "nop"


# =============================================================================
# Functions
# Execution
# =============================================================================

link = "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\08-des\\Game_Boot.txt"

Instructions = Formatting(link)


FixError(Instructions)
