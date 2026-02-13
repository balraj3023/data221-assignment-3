import pandas as pd
import numpy as np

crime = pd.read_csv("crime1.csv")
crime_column = crime["ViolentCrimesPerPop"]

# Compute statistical measures
mean_value = crime_column.mean()
median_value = crime_column.median()
std_value = crime_column.std()
min_value = crime_column.min()
max_value = crime_column.max()

# Print results
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_value)
print("Minimum:", min_value)
print("Maximum:", max_value)

# the mean is greater than the median by a small amount which means that the distribution is slightly right-skewed which means there are some higher crime values which pull the mean to be higher.
# the mean is more affected by extreme values because it includes all the numbers in its calculation, while the median is based only on the middle value.