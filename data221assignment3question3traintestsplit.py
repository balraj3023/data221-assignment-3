import pandas as pd
from sklearn.model_selection import train
kidney = pd.read_csv("kidney_disease.csv")
X = kidney.drop("classification", axis=1)
y = kidney["classification"]

# split into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

print("Training set size:", X_train.shape[0])
print("Testing set size:", X_test.shape[0])

# We should not train and test a model on the same data because the model could just memorize the answers. That would make it look accurate, but it wouldn’t perform well on new data.
# The testing set is used to check how well the model performs on data it has never seen before.
