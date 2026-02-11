import pandas as pd

dataframe = pd.read_csv("crime.csv")

# create risk column
dataframe["risk"] = "LowCrime"
dataframe.loc[dataframe["ViolentCrimesPerPop"] >= 0.50, "risk"] = "HighCrime"

# group by risk and compute average unemployment
grouped = dataframe.groupby("risk")["PctUnemployed"].mean()

# print results
for risk in grouped.index:
    print(risk + ": Average PctUnemployed =", grouped[risk])
