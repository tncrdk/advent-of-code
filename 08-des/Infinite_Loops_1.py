def Formatting(link):
    with open(link) as f:
        txt = f.read().split("\n")

    txt = [[i.split()[0], int(i.split()[1])] for i in txt]

    return txt


def FindBootError(Instructions: list):
    AlreadyDone = set()
    acc = 0
    Index = 0

    while True:
        if Index in AlreadyDone:
            print(acc)
            return

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


link = "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\08-des\\Game_Boot.txt"

Instructions = Formatting(link)

FindBootError(Instructions)
