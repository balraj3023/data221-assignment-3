import matplotlib.pyplot as plt

x = [2020,2022,2024,2026]
y = [5000000,3000000,7000000,2000000]

plt.plot(x, y, label='Data Science jobs in YYC', color = 'blue')
plt.title('Job market for Data Scientists in Calgary')
plt.legend() # uses the label
plt.show() # basically a print function for a graph


# plt.plot, line graph
# plt.scatter, dot graph
# plt.bar, bar graph