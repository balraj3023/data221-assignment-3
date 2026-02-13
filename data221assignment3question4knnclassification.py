import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

kidney = pd.read_csv("kidney_disease.csv")

# locate classification column robustly
cols_lower = {c.strip().lower(): c for c in kidney.columns}
target_col = cols_lower["classification"]

X = kidney.drop(columns=[target_col])
y_raw = kidney[target_col].astype(str).str.strip().str.lower()

# convert y to 0/1 in a safe way
label_map = {
    "0": 0, "1": 1,
    "ckd": 0, "notckd": 1,
    "ckd\t": 0, "notckd\t": 1
}
y = y_raw.map(label_map)

if y.isna().any():
    bad = sorted(y_raw[y.isna()].unique().tolist())
    raise ValueError(f"Unrecognized label values in classification: {bad}")

y = y.astype(int)

# train/test split (fixed random state)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

# clean X
missing_markers = ["?", " ? ", "", " ", "na", "n/a", "nan"]
X_train = X_train.replace(missing_markers, np.nan).apply(pd.to_numeric, errors="coerce")
X_test  = X_test.replace(missing_markers, np.nan).apply(pd.to_numeric, errors="coerce")

# drop columns that are all missing in training
all_nan_cols = X_train.columns[X_train.isna().all()]
X_train = X_train.drop(columns=all_nan_cols)
X_test  = X_test.drop(columns=all_nan_cols)

model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("knn", KNeighborsClassifier(n_neighbors=5))
])

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label=0, zero_division=0)
recall = recall_score(y_test, y_pred, pos_label=0, zero_division=0)
f1 = f1_score(y_test, y_pred, pos_label=0, zero_division=0)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

# True Positive means the model predicted CKD
# and the patient actually has CKD.
# True Negative means the model predicted notckd
# and the patient is actually healthy.
# False Positive means the model predicted CKD
# but the patient is actually healthy.
# False Negative means the model predicted healthy
# but the patient actually has CKD.

# Accuracy alone isn't enough since the database may have healthier patients than CKD patients.

# Recall is the most important metric because it measures how many actual CKD patients were correctly identified using the model.