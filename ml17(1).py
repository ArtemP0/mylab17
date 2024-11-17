from numpy import *
import pandas as pd

f = open("polygon.csv", "r")
list1 = []
list2 = []
list_ = [[], []]
f.readline()

data = f.readlines()
for i in range(len(data)):
    line1 = data[i].strip().split(",")
    name1, x1, y1 = line1[0], float(line1[1]), float(line1[2])
    line2 = data[(i + 1) % len(data)].strip().split(",")
    name2, x2, y2 = line2[0], float(line2[1]), float(line2[2])
    edge_name = name1 + "-" + name2
    list1.append(edge_name)
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    list2.append(distance)
f.close()

list_[0] = list1
list_[1] = list2
df = pd.DataFrame(list_)
df = df.T
df.to_csv("sides.csv", index=False, header=["Edge", "Length"])
print(df)
