import numpy as np
import time

with open(
    "C:\\Users\\thorb\\Documents\\Python\\Advent Of Code 2020\\02-des\\Passwords.txt"
) as f:
    arr = np.asarray(f.read().split(), str)

arr = arr.reshape(-1, 3)
counter = 0

for i in range(len(arr)):
    searchlist = arr[i, 2]
    search = arr[i, 1].strip(":")
    searchIndex = list(map(lambda a: int(a) - 1, arr[i, 0].split("-")))

    if (
        searchlist[searchIndex[0]] == search and searchlist[searchIndex[1]] != search
    ) or (
        searchlist[searchIndex[0]] != search and searchlist[searchIndex[1]] == search
    ):
        counter += 1

print(counter)
