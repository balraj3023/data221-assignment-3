threshold = 100
product = 1
currentNumber = 1

while product <= threshold:
    currentNumber = currentNumber + 1
    product *= currentNumber

print("Final product:",product)
print("Integer that exceeded the threshold:",currentNumber)
