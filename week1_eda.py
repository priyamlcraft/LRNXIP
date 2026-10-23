# LEARNIX MACHINE LEARNING INTERNSHIP
# WEEK 1: EXPLORATORY DATA INSPECTION
# Dataset: Iris Flower Dataset

# 1. Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# 2. Load the Iris dataset
iris = load_iris()

X = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

y = pd.Series(
    iris.target_names[iris.target],
    name="species"
)

# Combine features and labels
df = X.copy()
df["species"] = y

print("=" * 55)
print("LEARNIX INTERNSHIP - WEEK 1 PROJECT")
print("Exploratory Data Inspection")
print("=" * 55)

# 3. Inspect feature names and label
print("\n1. FEATURE COLUMN NAMES:")
print(X.columns.tolist())

print("\n2. OUTPUT LABEL:")
print(y.name)
print("Species classes:", iris.target_names)

# 4. Display the first five rows
print("\n3. FIRST FIVE ROWS:")
print(df.head())

# 5. Dataset information
print("\n4. DATASET SHAPE:")
print("Rows:", df.shape[0])
print("Columns including label:", df.shape[1])

print("\n5. DATA TYPES:")
print(df.dtypes)

# 6. Check missing values
print("\n6. MISSING VALUES:")
print(df.isnull().sum())

# 7. Statistical summary using Pandas and NumPy
print("\n7. STATISTICAL SUMMARY:")

summary = pd.DataFrame({
    "Minimum": X.min(),
    "Maximum": X.max(),
    "Average (Pandas)": X.mean(),
    "Average (NumPy)": np.mean(X.to_numpy(), axis=0)
})

print(summary.round(3))

# 8. Visual Plot 1: Scatter plot
print("\n8. CREATING SCATTER PLOT...")

plt.figure(figsize=(8, 5))

for species in iris.target_names:
    mask = y == species
    plt.scatter(
        X.loc[mask, "petal length (cm)"],
        X.loc[mask, "petal width (cm)"],
        label=species,
        alpha=0.8
    )

plt.title("Petal Length vs Petal Width")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.legend(title="Iris Species")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 9. Visual Plot 2: Histogram
print("\n9. CREATING HISTOGRAM...")

plt.figure(figsize=(8, 5))

plt.hist(
    X["petal length (cm)"],
    bins=15,
    edgecolor="black"
)

plt.title("Distribution of Petal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Number of Flowers")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# 10. Final observations
print("\n10. PROJECT SUMMARY:")
print("Total flower samples:", len(df))
print("Number of numerical features:", X.shape[1])
print("Number of species:", len(iris.target_names))
print("Species:", ", ".join(iris.target_names))
print("Total missing values:", int(df.isnull().sum().sum()))

print("\nProject execution completed successfully!")
