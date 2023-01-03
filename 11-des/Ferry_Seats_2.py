import pprint
import copy


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
    modkart = copy.deepcopy(kart)
    seatchange = False
    for y in range(len(kart)):
        for x in range(len(kart[0])):
            if kart[y][x] == "L":
                # vannrett
                adder = 1
                valid = True
                while True:
                    if kart[y][x + adder] == "#":
                        valid = False
                        break
                    if kart[y][x + adder] == "L":
                        break
                    if kart[y][x + adder] == "0":
                        break
                    adder += 1

                if not valid:
                    continue

                # vannrett
                adder = 1
                valid = True
                while True:
                    if kart[y][x - adder] == "#":
                        valid = False
                        break
                    if kart[y][x - adder] == "L":
                        break
                    if kart[y][x - adder] == "0":
                        break
                    adder += 1

                if not valid:
                    continue

                # loddrett
                adder = 1
                valid = True
                while True:
                    if kart[y + adder][x] == "#":
                        valid = False
                        break
                    if kart[y + adder][x] == "L":
                        break
                    if kart[y + adder][x] == "0":
                        break
                    adder += 1

                if not valid:
                    continue

                # loddrett
                adder = 1
                valid = True
                while True:
                    if kart[y - adder][x] == "#":
                        valid = False
                        break
                    if kart[y - adder][x] == "L":
                        break
                    if kart[y - adder][x] == "0":
                        break
                    adder += 1

                if not valid:
                    continue

                # diagonalhøyre
                adder = 1
                valid = True
                while True:
                    if kart[y + adder][x + adder] == "#":
                        valid = False
                        break
                    if kart[y + adder][x + adder] == "L":
                        break
                    if kart[y + adder][x + adder] == "0":
                        break
                    adder += 1

                if not valid:
                    continue

                # diagonalhøyre
                adder = 1
                valid = True
                while True:
                    if kart[y - adder][x + adder] == "#":
                        valid = False
                        break
                    if kart[y - adder][x + adder] == "L":
                        break
                    if kart[y - adder][x + adder] == "0":
                        break
                    adder += 1

                if not valid:
                    continue

                # diagonalvenstre
                adder = 1
                valid = True
                while True:
                    if kart[y + adder][x - adder] == "#":
                        valid = False
                        break
                    if kart[y + adder][x - adder] == "L":
                        break
                    if kart[y + adder][x - adder] == "0":
                        break
                    adder += 1

                if not valid:
                    continue

                # diagonalvenstre
                adder = 1
                valid = True
                while True:
                    if kart[y - adder][x - adder] == "#":
                        valid = False
                        break
                    if kart[y - adder][x - adder] == "L":
                        break
                    if kart[y - adder][x - adder] == "0":
                        break
                    adder += 1

                if not valid:
                    continue

                modkart[y][x] = "#"
                seatchange = True

            elif kart[y][x] == "#":
                # vannrett
                adder = 1
                counter = 0
                while True:
                    if kart[y][x + adder] == "#":
                        counter += 1
                        break
                    if kart[y][x + adder] == "L":
                        break
                    if kart[y][x + adder] == "0":
                        break
                    adder += 1

                # vannrett
                adder = 1
                while True:
                    if kart[y][x - adder] == "#":
                        counter += 1
                        break
                    if kart[y][x - adder] == "L":
                        break
                    if kart[y][x - adder] == "0":
                        break
                    adder += 1

                # loddrett
                adder = 1
                while True:
                    if kart[y + adder][x] == "#":
                        counter += 1
                        break
                    if kart[y + adder][x] == "L":
                        break
                    if kart[y + adder][x] == "0":
                        break
                    adder += 1

                # loddrett
                adder = 1
                while True:
                    if kart[y - adder][x] == "#":
                        counter += 1
                        break
                    if kart[y - adder][x] == "L":
                        break
                    if kart[y - adder][x] == "0":
                        break
                    adder += 1

                # diagonalhøyre
                adder = 1
                while True:
                    if kart[y + adder][x + adder] == "#":
                        counter += 1
                        break
                    if kart[y + adder][x + adder] == "L":
                        break
                    if kart[y + adder][x + adder] == "0":
                        break
                    adder += 1

                # diagonalhøyre
                adder = 1
                while True:
                    if kart[y - adder][x + adder] == "#":
                        counter += 1
                        break
                    if kart[y - adder][x + adder] == "L":
                        break
                    if kart[y - adder][x + adder] == "0":
                        break
                    adder += 1

                # diagonalvenstre
                adder = 1
                while True:
                    if kart[y + adder][x - adder] == "#":
                        counter += 1
                        break
                    if kart[y + adder][x - adder] == "L":
                        break
                    if kart[y + adder][x - adder] == "0":
                        break
                    adder += 1

                # diagonalvenstre
                adder = 1
                while True:
                    if kart[y - adder][x - adder] == "#":
                        counter += 1
                        break
                    if kart[y - adder][x - adder] == "L":
                        break
                    if kart[y - adder][x - adder] == "0":
                        break
                    adder += 1

                if counter >= 5:
                    modkart[y][x] = "L"
                    seatchange = True
    kart = copy.deepcopy(modkart)
    return seatchange


def Combined():
    counter = -1
    seatchange = True
    while seatchange == True:
        counter += 1
        seatchange = Updating()
        # pprint.pprint(Updating())

    occupied = [i.count("#") for i in kart]
    print(sum(occupied))


# =============================================================================
# Functions
# Execution
# =============================================================================

link = "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\11-des\\Ferry_Seats_1.txt"

kart = Formatting(link)


Combined()
