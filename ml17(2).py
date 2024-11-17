import pandas as pd
import json

data = []
with open("input.txt", "r") as f:
    for line in f:
        data.append(list(map(int, line.split())))

df = pd.DataFrame(data)
perimeter = []
perimeter += list(df.iloc[0])
perimeter += list(df.iloc[1:, -1])
perimeter += list(df.iloc[-1, :-1][::-1])
perimeter += list(df.iloc[-2:0:-1, 0])

with open("perimeter.json", "w") as f:
    json.dump(perimeter, f)

print("Збережено!")
