import pandas as pd

coronaDict: dict[str, list[str | int]] = {
    "Cities": ["Delhi", "Mumbai", "Chennai", "Surat"],
    "Cases": [3000, 4000, 5000, 4500],
}

# Creating DataFrame
CORONA: pd.DataFrame = pd.DataFrame(coronaDict, index=[100, 110, 120, 130])
print(CORONA)

# Adding recovery column

recovery = pd.Series([2000, 2000, 2000, 2000])
CORONA.loc[:, "Recovery"] = recovery
print(CORONA)

# Adding Deaths column using assign() method
CORONA = CORONA.assign(Deaths=[x * 1000 for x in range(1, 5)])
print(CORONA)

# Adding new row using loc
CORONA.loc[140, :] = ["Kolkata", 6000, 2000, 5000]
print(CORONA)

# Inserting percentage column using Insert
CORONA.insert(3, "Percentage", [15, 20, 25, 30, 35])
print(CORONA)

# Deleting percentage column using del
del CORONA["Percentage"]
print(CORONA)
