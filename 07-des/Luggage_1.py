def Formatting(link):
    with open(link) as f:
        txt = f.read().replace(".", "")
        txt = txt.replace(" bags", "")
        txt = txt.replace(" bag", "")
        txt = txt.replace("no other", "0 other")
        txt = txt.split("\n")
    txt = [i.split(" contain ") for i in txt]
    for i in txt:
        i[1] = i[1].split(", ")

    AllDicts = {}
    for i in txt:
        AllDicts.update({i[0]: {x[2:]: int(x[0]) for x in i[1]}})

    return AllDicts


def Shiny_Gold_Carriers(
    AllDicts: dict, Already_Checked: set, Dict_To_Check: str, Correct_Bags: set
):
    for i in AllDicts[Dict_To_Check].values():
        if i == 0:
            Already_Checked.add(Dict_To_Check)
            return Already_Checked, Correct_Bags, False

    if Dict_To_Check in Already_Checked and Dict_To_Check in Correct_Bags:
        return Already_Checked, Correct_Bags, True

    if Dict_To_Check in Already_Checked:
        return Already_Checked, Correct_Bags, False

    for i in AllDicts[Dict_To_Check]:
        return_values = Shiny_Gold_Carriers(AllDicts, Already_Checked, i, Correct_Bags)
        try:
            Correct_Bags = Correct_Bags | return_values[1]
        except:
            pass
        try:
            Already_Checked = Already_Checked | return_values[0]
        except:
            pass

        Already_Checked.add(Dict_To_Check)

        if return_values[2]:
            Correct_Bags.add(Dict_To_Check)
            return Already_Checked, Correct_Bags, True

    if "shiny gold" == Dict_To_Check:
        return Already_Checked.add(Dict_To_Check), Correct_Bags, True

    return Already_Checked, Correct_Bags, False


def Check_Every_Luggage(AllDicts):
    Already_Checked = set()
    Correct_Bags = set()
    a = True
    for i in AllDicts:
        return_values = Shiny_Gold_Carriers(AllDicts, Already_Checked, i, Correct_Bags)
        try:
            Already_Checked = Already_Checked | return_values[0]
        except:
            pass
        try:
            Correct_Bags = Correct_Bags | return_values[1]
        except:
            pass

    print(len(Correct_Bags))


# =============================================================================
# Functions
# Execution
# =============================================================================


link = "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\07-des\\Luggage_Rules.txt"

AllDicts = Formatting(link)

Check_Every_Luggage(AllDicts)
