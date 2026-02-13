import os
from os import path

filepath = os.path.join(os.getcwd(), "utils", "items.dcc")
print(filepath)
file = open(filepath, "r", encoding="utf-8")
for line in file:
    print(line, end="")