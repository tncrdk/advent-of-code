def Formatting(link):
    with open(link) as f:
        txt = [int(i) for i in f.read().split()]
    txt.sort()
    txt.insert(0, 0)

    return txt


def Combinations(index):
    global already_checked
    global joltage_rates

    if index in already_checked:
        return already_checked[index]

    if index >= len(joltage_rates) - 2:
        already_checked[index] = 1
        return 1

    if joltage_rates[index + 1] - joltage_rates[index] <= 3:
        combi = Combinations(index + 1)

    if joltage_rates[index + 2] - joltage_rates[index] <= 3:
        combi += Combinations(index + 2)

        if index + 2 < len(joltage_rates) - 1:
            if joltage_rates[index + 3] - joltage_rates[index] <= 3:
                combi += Combinations(index + 3)

    already_checked[index] = combi

    return combi


# =============================================================================
# Functions
# Execution
# =============================================================================

link = "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\10-des\\joltage_rates.txt"

joltage_rates = Formatting(link)

already_checked = {}

print(Combinations(0))
