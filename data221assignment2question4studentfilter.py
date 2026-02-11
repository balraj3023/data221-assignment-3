import pandas as pd

dataframe = pd.read_csv("student.csv")

# filter high-engagement students
filtered = dataframe[
    (dataframe["studytime"] >= 3) &
    (dataframe["internet"] == 1) &
    (dataframe["absences"] <= 5)
]

# save to new file
filtered.to_csv("high_engagement.csv", index=False)

# print required outputs
print("Number of students saved:", len(filtered))
print("Average grade:", filtered["grade"].mean())