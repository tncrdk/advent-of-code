def Formatting(link):
    with open(link) as f:
        txt = f.read()
    return txt.split()


def FindRow(directions, Rows):
    for i in directions:
        Steps = int(len(Rows) / 2)
        if i == "F":
            Rows = Rows[0:Steps]
        elif i == "B":
            Rows = Rows[Steps:]

    return Rows


def FindSeat(directions, Seats):
    for i in directions:
        Steps = int(len(Seats) / 2)
        if i == "L":
            Seats = Seats[0:Steps]
        elif i == "R":
            Seats = Seats[Steps:]

    return Seats


def FindMissingID(directionsList):
    Rows = [i for i in range(0, 128)]
    Seats = [i for i in range(0, 8)]
    Highest_SeatID = 0
    SeatIDList = []

    for i in directionsList:
        RowNum = FindRow(i[:7], Rows)[0]
        SeatNum = FindSeat(i[7:], Seats)[0]
        SeatID = RowNum * 8 + SeatNum

        if RowNum != 127 or RowNum != 0:
            SeatIDList.append(SeatID)

    CompleteList = set([i for i in range(16, 835)])
    MySeat = CompleteList - set(SeatIDList)
    print(MySeat)


link = (
    "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\05-des\\Seats_List.txt"
)

directionsList = Formatting(link)

FindMissingID(directionsList)
