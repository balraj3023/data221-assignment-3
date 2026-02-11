import matplotlib.pyplot as plt
x = [1, 2, 1.5, 2.1, 2.2, 2.5, 3, 2, 2
, 2.6, 3, 2, 1.5, 2.5, 4]
plt.boxplot(x)
#plt.show()

for i in x:
    sum = 0
    sum += i
    avg =  sum / len(x)
print(avg)
