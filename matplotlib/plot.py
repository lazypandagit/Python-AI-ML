import pandas as pd
import matplotlib.pyplot as plt


pd.options.display.float_format = "{:.2f}".format
df = pd.read_csv("./matplot/data1.csv")


genderedMean = df[["Gender", "Salary"]].groupby("Gender").mean()
print(genderedMean)


# bar
barplt = plt.figure(figsize=(5, 5))
bars = plt.bar(
    genderedMean.index,
    genderedMean["Salary"],
    width=0.4,
    color=["#d5a6bd", "#6fa8dc"],
    edgecolor=["Black"],
)
# bar labels
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width() / 2, yval, yval, ha="center", va="bottom")

plt.xlabel("Genders")
plt.ylabel("Average Salary")
plt.title("Gender wise salary breack-up")
plt.show()


# Scatter
scater = plt.figure(figsize=(5, 5))
plt.scatter(df["Age"], df["Salary"])
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age Vs Salary")
plt.show()

# histogram
sal = df["Salary"]
plt.hist(sal, bins=100)

# Add labels and title
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram with 20 Bins")

# Show plot
plt.show()

