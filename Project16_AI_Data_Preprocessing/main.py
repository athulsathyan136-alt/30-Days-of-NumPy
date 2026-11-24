
import numpy as np

# =========================================
# 1. LOAD DATASET
# =========================================

data = np.genfromtxt(
    "data/student_data.csv",
    delimiter=",",
    skip_header=1,
    dtype=str
)

student_ids = data[:, 0].astype(int)
age = data[:, 1].astype(float)
study_hours = data[:, 2].astype(float)
attendance = data[:, 3].astype(float)
previous_score = data[:, 4].astype(float)
internet = data[:, 5]
final_score = data[:, 6].astype(float)

print("\n===== AI DATA PREPROCESSING =====")
print("Dataset shape:", data.shape)

# =========================================
# 2. MISSING VALUE HANDLING
# =========================================

# Example missing value for demonstration
study_hours[2] = np.nan

missing_count = np.isnan(study_hours).sum()

print("\nMissing values:", missing_count)

study_mean = np.nanmean(study_hours)

study_hours = np.nan_to_num(
    study_hours,
    nan=study_mean
)

print("Missing values replaced:", np.isnan(study_hours).sum())

# =========================================
# 3. OUTLIER DETECTION
# =========================================

q1 = np.percentile(final_score, 25)
q3 = np.percentile(final_score, 75)

iqr = q3 - q1

lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

outlier_positions = np.where(
    (final_score < lower_limit) |
    (final_score > upper_limit)
)[0]

print("\n===== OUTLIER DETECTION =====")
print("Lower limit:", lower_limit)
print("Upper limit:", upper_limit)
print("Outlier positions:", outlier_positions)

# =========================================
# 4. FEATURE NORMALIZATION
# =========================================

numerical_features = np.column_stack((
    age,
    study_hours,
    attendance,
    previous_score
))

feature_min = np.min(numerical_features, axis=0)
feature_max = np.max(numerical_features, axis=0)

normalized_features = (
    numerical_features - feature_min
) / (feature_max - feature_min)

print("\n===== NORMALIZATION =====")
print(normalized_features)

# =========================================
# 5. FEATURE STANDARDIZATION
# =========================================

feature_mean = np.mean(
    numerical_features,
    axis=0
)

feature_std = np.std(
    numerical_features,
    axis=0
)

# Avoid division by zero for constant features
feature_std = np.where(
    feature_std == 0,
    1,
    feature_std
)

standardized_features = (
    numerical_features - feature_mean
) / feature_std

print("\n===== STANDARDIZATION =====")
print(standardized_features)

# =========================================
# 6. CATEGORICAL ENCODING
# =========================================

internet_encoded = np.where(
    internet == "Yes",
    1,
    0
)

print("\n===== CATEGORICAL ENCODING =====")
print(internet_encoded)

# =========================================
# 7. FEATURE ENGINEERING
# =========================================

study_efficiency = (
    study_hours * attendance
) / 100

performance_gap = (
    final_score - previous_score
)

new_features = np.column_stack((
    study_efficiency,
    performance_gap
))

print("\n===== NEW FEATURES =====")
print(new_features)

# =========================================
# 8. FINAL FEATURE MATRIX
# =========================================

X = np.column_stack((
    normalized_features,
    internet_encoded,
    new_features
))

y = final_score

print("\nFeature matrix shape:", X.shape)
print("Target shape:", y.shape)

# =========================================
# 9. TRAIN TEST SPLIT
# =========================================

rng = np.random.default_rng(42)

indices = rng.permutation(len(X))

split_position = int(len(X) * 0.8)

train_indices = indices[:split_position]
test_indices = indices[split_position:]

X_train = X[train_indices]
X_test = X[test_indices]

y_train = y[train_indices]
y_test = y[test_indices]

print("\n===== DATA SPLIT =====")

print("Training features:", X_train.shape)
print("Testing features:", X_test.shape)
print("Training targets:", y_train.shape)
print("Testing targets:", y_test.shape)

# =========================================
# 10. SAVE PROCESSED DATA
# =========================================

np.save("outputs/X_train.npy", X_train)
np.save("outputs/X_test.npy", X_test)
np.save("outputs/y_train.npy", y_train)
np.save("outputs/y_test.npy", y_test)

np.savetxt(
    "outputs/processed_features.csv",
    X,
    delimiter=",",
    fmt="%.4f"
)

print("\nAll preprocessing outputs saved!")
