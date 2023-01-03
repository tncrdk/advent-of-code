import numpy as np

with open(
    "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\01-des\Tall.txt"
) as f:
    arr = list(map(int, f.read().split()))

arr = np.asarray(arr)

for i in arr:
    if 2020 - i in arr:
        print(i * (2020 - i))
        break
