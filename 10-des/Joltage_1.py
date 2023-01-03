def Formatting(link):
    with open(link) as f:
        txt = [int(i) for i in f.read().split()]
    txt.sort()
    txt.insert(0, 0)
    txt.append(txt[-1] + 3)

    return txt


def JoltDifferences(joltage_rates):
    rates_1 = 0
    rates_3 = 0

    for i in range(1, len(joltage_rates)):
        diff = joltage_rates[i] - joltage_rates[i - 1]
        if diff == 3:
            rates_3 += 1
        elif diff == 1:
            rates_1 += 1

    print(rates_1 * rates_3)


# =============================================================================
# Functions
# Execution
# =============================================================================

link = "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\10-des\\joltage_rates.txt"

joltage_rates = Formatting(link)

JoltDifferences(joltage_rates)
