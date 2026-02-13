import pandas as pd
import matplotlib.pyplot as plt

crime = pd.read_csv("crime1.csv")
crime_column = crime["ViolentCrimesPerPop"]

# histograph
plt.figure()
plt.hist(crime_column, bins=20, edgecolor="black")
plt.title("Histogram of Violent Crimes Per Population")
plt.xlabel("ViolentCrimesPerPop")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()

# box plot
plt.figure()
plt.boxplot(crime_column)
plt.title("Box Plot of Violent Crimes Per Population")
plt.ylabel("ViolentCrimesPerPop")
plt.savefig("boxplot.png")
plt.show()

# the histograph shows how the crime rates are spread out per population. Most communities are within a similar range with some having an excess amount of crime, while some have a lower crime rate.
# In the box plot, the median line appears lower than the mean, which suggests the data is slightly right-skewed meaning that there are some higher crime-rates that make the mean higher than the median.
# The box plot doesn't show any points outside which indicates there are no outliers in the data