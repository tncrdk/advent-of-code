def Formatting(link):
    with open(link) as f:
        txt = (
            f.read()
            .replace(".", "")
            .replace(" bags", "")
            .replace(" bag", "")
            .replace("no other", "0 other")
        )
        txt = txt.split("\n")
    txt = [i.split(" contain ") for i in txt]
    for i in txt:
        i[1] = i[1].split(", ")

    AllDicts = {}
    for i in txt:
        AllDicts.update({i[0]: {x[2:]: int(x[0]) for x in i[1]}})

    return AllDicts


def Total_Luggage(
    AllDicts: dict, Already_Checked: set, Dict_To_Check: str, Total_Bags: dict
):
    for i in AllDicts[Dict_To_Check].values():
        if i == 0:
            Already_Checked.add(Dict_To_Check)
            Total_Bags.update({Dict_To_Check: 0})
            return Already_Checked, Total_Bags, 0

    if Dict_To_Check in Already_Checked:
        return Already_Checked, Total_Bags, Total_Bags[Dict_To_Check]

    luggage = 0
    for i in AllDicts[Dict_To_Check]:
        return_values = Total_Luggage(AllDicts, Already_Checked, i, Total_Bags)
        try:
            Already_Checked = Already_Checked | return_values[0]
        except:
            pass
        try:
            Total_Bags = return_values[1]
        except:
            pass

        luggage += (
            AllDicts[Dict_To_Check][i] + AllDicts[Dict_To_Check][i] * return_values[2]
        )

    Total_Bags.update({Dict_To_Check: luggage})

    return Already_Checked, Total_Bags, Total_Bags[Dict_To_Check]


def Golden_Bag(AllDicts):
    Already_Checked = set()
    Total_Bags = {}
    return_values = Total_Luggage(AllDicts, Already_Checked, "shiny gold", Total_Bags)
    print(return_values[2])


# =============================================================================
# Functions
# Execution
# =============================================================================


link = "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\07-des\\Luggage_Rules.txt"

AllDicts = Formatting(link)

Golden_Bag(AllDicts)
