import pandas as pd

# dictionary for item table
items: dict[str, list[int | str]] = {
    "itemID": ["PC01", "LC05", "PC03", "PC06", "LC03"],
    "itemName": [
        "Personal Computer",
        "Laptop",
        "Personal Computer",
        "Personal Computer",
        "Laptop",
    ],
    "manufacturer": ["HCL India", "HP USA", "Dell USA", "Zenith USA", "Dell USA"],
    "price": [42000, 55000, 32000, 37000, 57000],
}

# dcitionary for "Customer" table
customer: dict[str, list[str]] = {
    "item_ID": ["LC03", "PC03", "PC06", "LC03", "PC01"],
    "customerName": ["N Roy", "H Singh", "R Pandey", "C Sharma", "K Agarwal"],
    "city": ["Delhi", "Mumbai", "Delhi", "Chennai", "Bengaluru"],
}

# ============================================#
# creating DataFrame for items
dfI: pd.DataFrame = pd.DataFrame(items)
print(f"\nItems Table:-\n{dfI}")
# ============================================#

# ---------------------------------------------
# creating DataFrame for Customers
dfC: pd.DataFrame = pd.DataFrame(customer)
print(f"\nCustomers:-\n{dfC}")
# ---------------------------------------------

##############################################
# default join on dfI and dfC
concatDf = pd.concat([dfC, dfI], axis=1, join="outer")
print(f"\njoined df:-\n{concatDf}")
##############################################

# --------------------------------------------#
# left join
leftJoin = pd.merge(dfC, dfI, how="inner", left_on="item_ID", right_on="itemID")
print(f"\n Left join DF:-\n{leftJoin}")
# ---------------------------------------------#
