def Formatting(link):
    with open(link) as f:
        txt = f.read().replace(" ", "\n")

    txt = txt.split("\n\n")
    txt = [i.split() for i in txt]

    AllDicts = []
    for passport in txt:
        Dict = {passport[i][:3]: passport[i][4:] for i in range(len(passport))}
        AllDicts.append(Dict)

    return AllDicts


def CheckAllKeysExist(AllDicts: list, Keys: list):
    ValidDicts = []
    for dictionary in AllDicts:
        exist = True
        for key in Keys:
            if key not in dictionary:
                exist = False
        if exist:
            ValidDicts.append(dictionary)

    return ValidDicts


def CorrectInfo(Dictionary: dict):
    Eyecolors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    Symbols = [str(i) for i in range(0, 10)] + ["a", "b", "c", "d", "e", "f"] + ["#"]
    Numbers = [str(i) for i in range(0, 10)]

    if int(Dictionary["byr"]) < 1920 or int(Dictionary["byr"]) > 2002:
        return False
    if int(Dictionary["iyr"]) < 2010 or int(Dictionary["iyr"]) > 2020:
        return False
    if int(Dictionary["eyr"]) < 2020 or int(Dictionary["eyr"]) > 2030:
        return False
    if len(Dictionary["pid"]) != 9 or len(set(Dictionary["pid"]) - set(Numbers)) != 0:
        return False
    if (
        len(set(Dictionary["hcl"]) - set(Symbols)) != 0
        or len(Dictionary["hcl"]) != 7
        or Dictionary["hcl"][0] != "#"
    ):
        return False
    if Dictionary["hgt"][-2:] == "cm":
        if (
            int(Dictionary["hgt"].split("c")[0]) < 150
            or int(Dictionary["hgt"].split("c")[0]) > 193
        ):
            return False
    if Dictionary["hgt"][-2:] == "in":
        if (
            int(Dictionary["hgt"].split("i")[0]) < 59
            or int(Dictionary["hgt"].split("i")[0]) > 76
        ):
            return False
    if Dictionary["hgt"][-2:] != "in" and Dictionary["hgt"][-2:] != "cm":
        return False
    if len({Dictionary["ecl"]} - Eyecolors) != 0 or len(Dictionary["ecl"]) != 3:
        return False

    return True


def CheckEveryDict(link, Validkeys):
    AllDicts = Formatting(link)

    AllDicts = CheckAllKeysExist(AllDicts, Validkeys)
    counter = 0

    for i in AllDicts:
        if CorrectInfo(i):
            counter += 1

    print(counter)


# =============================================================================
# Functions
# Execution
# =============================================================================

link = "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\04-des\\PassPorts.txt"

Validkeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

CheckEveryDict(link, Validkeys)
