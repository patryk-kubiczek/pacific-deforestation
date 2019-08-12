#!/usr/bin/env python
"""
This script cleans the datasets needed for analysis
"""
import os
import pandas as pd
import yaml
from numpy import NaN

# Get config file
conf = {k: v for d in yaml.safe_load(open('conf.yaml')) for k, v in d.items()}

names = ["Atkinson2016.xlsx", "Rollet2004.xls"]
filenames = [os.path.join(conf["data"]["raw"], name) for name in names]
clean_names = ["Atkinson2016.csv", "Rollet2004.csv"]

# Atkinson 2016
print("Creating dataset", clean_names[0])

data1 = pd.read_excel(filenames[0], sheet_name="Deforestation Data")
data1_replacement = pd.read_excel(filenames[0], sheet_name="Replacement Data", usecols=[2])
data1.insert(2, "Replacement", data1_replacement)

data1.Island = data1.Island.str.replace("(wind)", " (wind.)", regex=False)
data1.Island = data1.Island.str.replace("(lee)", " (lee.)", regex=False)
data1.Island = data1.Island.str.replace("(E coast)", " (E coast)", regex=False)
data1.Island = data1.Island.str.replace("(W coast)", " (W coast)", regex=False)
data1.Island = data1.Island.str.replace("S. Island", "South Island", regex=False)

data1.rename(columns={"Age": "Age=3"}, inplace=True)

data1.to_csv(os.path.join(conf["data"]["int"], clean_names[0]))

# Rollet 2004
print("Creating dataset:", clean_names[1])

col_names = ["Number", "Archipelago", "Island", "Replacement", "Deforestation",
             "Area", "Area 50", "Isolation", "Isolation 75", "Elevation",
             "Latitude", "Rainfall", "Age", "Makatea", "Dust", "Tephra"]
cols = [i for i in range(18) if i not in [6, 9]]
data2 = pd.read_excel(filenames[1], usecols=cols, index_col=0, skiprows=11,
                      header=None, names=col_names)

data2.Island = data2.Island.str.replace("(lee)", "(lee.)", regex=False)
data2.Island = data2.Island.str.replace("(wind)", "(wind.)", regex=False)
data2.Island = data2.Island.str.replace("S. Island", "South Island", regex=False)

data2.Latitude = data2.Latitude.str.replace("^[0-9. ]*S$", lambda s : "-" + s.group(0)[:-1], regex=True)
data2.Latitude = data2.Latitude.str.replace("^[0-9. ]*N$", lambda s : "+" + s.group(0)[:-1], regex=True)
data2.Latitude = data2.Latitude.astype(float)

data2.Rainfall = data2.Rainfall.astype(str).str.replace("ca. ", "", regex=False)
data2["Isolation 75"].replace("none", NaN, inplace=True)
data2.Age.replace("X", NaN, inplace=True)
# Fix typo (lee -> wind)
data2.loc[80, "Island"] = "Mangareva (wind.)"

data2.set_index("Island", drop=True, inplace=True)

# Fix typo (missing N or S -> S (-))
data2.loc["Tahiti", "Latitude"] = -17.5
# Fix island name so it coincides with dataset 1
data2.rename(index={"Fatuiva" : "Fatu Hiva"}, inplace=True)
data2["Archipelago"].replace("W Poly", "W Polynesia", inplace=True)

data2.to_csv(os.path.join(conf["data"]["int"], clean_names[1]))
