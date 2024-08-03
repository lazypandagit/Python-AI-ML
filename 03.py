import pandas as pd

sale = {
    2020: {"Q1": 3000, "Q2": 3500, "Q3": 2700, "Q4": 4200},
    2022: {"Q1": 1900, "Q2": 3400, "Q3": 2600, "Q4": 1800},
    2024: {"Q1": 1580, "Q2": 3800, "Q3": 3400, "Q4": 2700},
}

df = pd.DataFrame(sale)
# print("Iterating over rows\n")
# for rowIndex, rowValues in df.iterrows():
#     print(f"Row {rowIndex} = \n{rowValues}")


# print("\nIterating over columns\n")
# for columnIndex, columnValues in df.items():
#     print(f"Values in column {columnIndex}= \n{columnValues}")

for columnIndex, columnValues in df.items():
    max = 0
    for sales in columnValues.items():
        if sales[1] > max:
            max = sales[1]
            maxq = sales.index
    print(f"maximum sale for the year {columnIndex} is {max}")
