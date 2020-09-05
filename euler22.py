import pandas as pd
import numpy as np 

FILEPATH = "names.txt"

with open(FILEPATH) as f:
    names = f.readline().replace('"', '')
    names = sorted(names.split(","))

def sum_letters(name):
    return sum(ord(letter)-64 for letter in name)

names = pd.DataFrame(data=names, columns=["names"])
names["vals"] = names["names"].apply(sum_letters)
names["vals_index"] = names["vals"] * (names.index + 1)

total = names["vals_index"].sum()
print(total)