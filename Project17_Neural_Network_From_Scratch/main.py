
import numpy as np

# ==========================================
# 1. LOAD DATASET
# ==========================================

data = np.genfromtxt(
    "data/student_pass.csv",
    delimiter=",",
    skip_header=1
)

X = data[:, :3]
y = data[:, 3].reshape(-1, 1)

# Normalize input features
X = X / np.array([11, 100, 100])

# ==========================================
# 2. NETWORK CONFIGURATION
# ==========================================

input_neurons = 3
hidden_neurons = 4
output_neurons = 1

learning_rate = 0.1
epochs = 5000

rng = np.random.default_rng(42)

# Initialize weights and biases
W1 = rng.normal(0, 0.5, (input_neurons, hidden_neurons))
b1 = np.zeros((1, hidden_neurons))

W2 = rng.normal(0, 0.5, (hidden_neurons, output_neurons))
b2 = np.zeros((1, output_neurons))

# ==========================================
# 3. ACTIVATION FUNCTIONS
# ==========================================

def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):
    return (x > 0).astype(float)


def sigmoid(x):
    x = np.clip(x, -500, 500)
    return 1 / (1 + np.exp(-x))


# ==========================================
# 4. TRAINING LOOP
# ==========================================

for epoch in range(epochs):

    # FORWARD PROPAGATION

    z1 = np.dot(X, W1) + b1
    a1 = relu(z1)

    z2 = np.dot(a1, W2) + b2
    predictions = sigmoid(z2)

    # LOSS

    epsilon = 1e-8

    loss = -np.mean(
        y * np.log(predictions + epsilon)
        + (1 - y) * np.log(1 - predictions + epsilon)
    )

    # BACKPROPAGATION

    m = len(X)

    dz2 = (predictions - y) / m

    dW2 = np.dot(a1.T, dz2)
    db2 = np.sum(dz2, axis=0, keepdims=True)

    dz1 = np.dot(dz2, W2.T) * relu_derivative(z1)

    dW1 = np.dot(X.T, dz1)
    db1 = np.sum(dz1, axis=0, keepdims=True)

    # GRADIENT DESCENT

    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

    if (epoch + 1) % 500 == 0:
        print(
            "Epoch:", epoch + 1,
            "Loss:", round(float(loss), 4)
        )

# ==========================================
# 5. FINAL PREDICTIONS
# ==========================================

z1 = np.dot(X, W1) + b1
a1 = relu(z1)

z2 = np.dot(a1, W2) + b2
predictions = sigmoid(z2)

predicted_classes = (predictions >= 0.5).astype(int)

accuracy = np.mean(predicted_classes == y) * 100

print("\n===== MODEL RESULTS =====")

print("Accuracy:", accuracy, "%")
print("Final loss:", loss)

# ==========================================
# 6. SAVE MODEL PARAMETERS
# ==========================================

np.savez(
    "outputs/neural_network_model.npz",
    W1=W1,
    b1=b1,
    W2=W2,
    b2=b2
)

# Save prediction report
report = np.column_stack((
    y.flatten(),
    predictions.flatten(),
    predicted_classes.flatten()
))

np.savetxt(
    "outputs/predictions.csv",
    report,
    delimiter=",",
    header="Actual,Probability,Predicted",
    comments="",
    fmt="%.4f"
)

print("\nModel and predictions saved!")
