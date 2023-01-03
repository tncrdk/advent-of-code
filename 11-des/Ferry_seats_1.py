import pprint


def Formatting(link):
    with open(link) as f:
        txt = f.read().split()
    txt = ["0" + i + "0" for i in txt]
    txt.append("0" * (len(txt[0])))
    txt.insert(0, "0" * (len(txt[0])))
    txt = [[x for x in i] for i in txt]

    return txt


def Updating():
    global kart
    change = []
    seatchange = False
    for y in range(len(kart)):
        for x in range(len(kart[0])):
            if kart[y][x] == "L":
                if kart[y][x - 1] == "#":
                    continue
                if kart[y][x + 1] == "#":
                    continue
                if kart[y - 1][x] == "#":
                    continue
                if kart[y + 1][x] == "#":
                    continue
                if kart[y - 1][x - 1] == "#":
                    continue
                if kart[y + 1][x - 1] == "#":
                    continue
                if kart[y + 1][x + 1] == "#":
                    continue
                if kart[y - 1][x + 1] == "#":
                    continue
                change.append((y, x))
                seatchange = True

            elif kart[y][x] == "#":
                seats = 0
                if kart[y][x - 1] == "#":
                    seats += 1
                if kart[y][x + 1] == "#":
                    seats += 1
                if kart[y - 1][x] == "#":
                    seats += 1
                if kart[y + 1][x] == "#":
                    seats += 1
                if kart[y - 1][x - 1] == "#":
                    seats += 1
                if kart[y + 1][x - 1] == "#":
                    seats += 1
                if kart[y + 1][x + 1] == "#":
                    seats += 1
                if kart[y - 1][x + 1] == "#":
                    seats += 1

                if seats >= 4:
                    change.append((y, x))
                    seatchange = True

    return seatchange, change


def Updating2(change):
    global kart
    for i in change:
        if kart[i[0]][i[1]] == "L":
            kart[i[0]][i[1]] = "#"
        elif kart[i[0]][i[1]] == "#":
            kart[i[0]][i[1]] = "L"

    return kart


def Combined():
    counter = -1
    seatchange = True
    while seatchange == True:
        counter += 1
        seatchange, change = Updating()
        kart = Updating2(change)
        # pprint.pprint(kart)

    occupied = [i.count("#") for i in kart]
    print(sum(occupied))


# =============================================================================
# Functions
# Execution
# =============================================================================

link = "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\11-des\\Ferry_Seats_1.txt"

kart = Formatting(link)
# print(kart)
Combined()
