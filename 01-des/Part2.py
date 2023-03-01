import numpy as np

with open(
    "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\01-des\Tall.txt"
) as f:
    arr = np.asarray(list(map(int, f.read().split())))


def foo(arr):
    for i in arr:
        for a in arr:
            if 2020 - (a + i) > 1:
                if 2020 - (a + i) in arr:
                    return a * i * (2020 - (a + i))

print(foo(arr))
print(foo(arr))
