import pandas as pd

# load data
dataframe = pd.read_csv("student.csv")

# create grade_band column
bands = []

for g in dataframe["grade"]:
    if g <= 9:
        bands.append("Low")
    elif g <= 14:
        bands.append("Medium")
    else:
        bands.append("High")

dataframe["grade_band"] = bands

# group and calculate summary values
grouped = dataframe.groupby("grade_band")

summary = grouped.agg(
    students=("grade", "count"),
    avg_absences=("absences", "mean"),
    internet_pct=("internet", "mean")
)

# convert internet fraction to percentage
summary["internet_pct"] = summary["internet_pct"] * 100

# save result
summary.to_csv("student_bands.csv")

# display summary
print(summary)
