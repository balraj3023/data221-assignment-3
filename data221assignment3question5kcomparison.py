import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


kidney = pd.read_csv("kidney_disease.csv")

# Find classification column
cols_lower = {c.strip().lower(): c for c in kidney.columns}
target_col = cols_lower["classification"]

X = kidney.drop(columns=[target_col])
y = kidney[target_col].astype(str).str.strip().str.lower()

# convert labels to 0/1
y = y.replace({"ckd": 0, "notckd": 1, "0": 0, "1": 1}).astype(int)

# train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

# clean features
X_train = X_train.replace(["?", " ? ", "", " "], np.nan).apply(pd.to_numeric, errors="coerce")
X_test  = X_test.replace(["?", " ? ", "", " "], np.nan).apply(pd.to_numeric, errors="coerce")

# Drop columns that are fully missing
all_nan_cols = X_train.columns[X_train.isna().all()]
X_train = X_train.drop(columns=all_nan_cols)
X_test  = X_test.drop(columns=all_nan_cols)
k_values = [1, 3, 5, 7, 9]
results = []

for k in k_values:
    model = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("knn", KNeighborsClassifier(n_neighbors=k))
    ])

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results.append((k, acc))

results_df = pd.DataFrame(results, columns=["k", "Test Accuracy"])
print(results_df)

best_row = results_df.loc[results_df["Test Accuracy"].idxmax()]
print("Best k:", best_row["k"])
print("Highest Accuracy:", best_row["Test Accuracy"])

# Changing k affects how sensitive the model is.
# Small k values can overfit because they focus too much on nearby points.
# Large k values can underfit because they smooth out important patterns.

