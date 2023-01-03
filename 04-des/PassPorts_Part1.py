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


def CheckAllKeysExist(link: str, Keys: list):
    AllDicts = Formatting(link)
    ValidDicts = []
    for dictionary in AllDicts:
        exist = True
        for key in Keys:
            if key not in dictionary:
                exist = False
        if exist:
            ValidDicts.append(dictionary)

    print(len(ValidDicts))


# =============================================================================
# Functions
# Execution
# =============================================================================

link = "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\04-des\\PassPorts.txt"

Valid = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

CheckAllKeysExist(link, Valid)
