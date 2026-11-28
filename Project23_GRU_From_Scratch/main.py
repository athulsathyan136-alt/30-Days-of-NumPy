import numpy as np
from pathlib import Path

# =====================================
# 1. Project setup
# =====================================

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

rng = np.random.default_rng(42)

# =====================================
# 2. Generate sequence dataset
# =====================================

def create_dataset(samples=1000, sequence_length=5):

    X = rng.uniform(
        0,
        1,
        size=(samples, sequence_length, 1)
    )

    averages = X.mean(axis=(1, 2))

    y = (averages >= 0.5).astype(int)

    return X, y

X, y = create_dataset()

# Shuffle before splitting
indices = rng.permutation(len(X))

X = X[indices]
y = y[indices]

split = int(0.8 * len(X))

X_train = X[:split]
y_train = y[:split]

X_test = X[split:]
y_test = y[split:]

print("Training shape:", X_train.shape)
print("Testing shape:", X_test.shape)

# =====================================
# 3. Model configuration
# =====================================

input_size = 1
hidden_size = 12
output_size = 2

learning_rate = 0.01
epochs = 120

def initialize_weights(rows, columns):

    return rng.normal(
        0,
        0.1,
        size=(rows, columns)
    )

# Update gate
W_xz = initialize_weights(hidden_size, input_size)
W_hz = initialize_weights(hidden_size, hidden_size)
b_z = np.zeros((hidden_size, 1))

# Reset gate
W_xr = initialize_weights(hidden_size, input_size)
W_hr = initialize_weights(hidden_size, hidden_size)
b_r = np.zeros((hidden_size, 1))

# Candidate hidden state
W_xn = initialize_weights(hidden_size, input_size)
W_hn = initialize_weights(hidden_size, hidden_size)
b_n = np.zeros((hidden_size, 1))

# Output layer
W_y = initialize_weights(output_size, hidden_size)
b_y = np.zeros((output_size, 1))

# =====================================
# 4. Activation functions
# =====================================

def sigmoid(x):

    x = np.clip(x, -50, 50)

    return 1 / (1 + np.exp(-x))

def softmax(x):

    x = x - np.max(x)

    exp_values = np.exp(x)

    return exp_values / np.sum(exp_values)

# =====================================
# 5. GRU forward propagation
# =====================================

def forward(sequence):

    h = np.zeros((hidden_size, 1))

    cache = []

    for value in sequence:

        x = np.array([[value]])

        previous_h = h.copy()

        # Update gate
        z = sigmoid(
            W_xz @ x + W_hz @ h + b_z
        )

        # Reset gate
        r = sigmoid(
            W_xr @ x + W_hr @ h + b_r
        )

        # Candidate hidden state
        n = np.tanh(
            W_xn @ x
            + W_hn @ (r * h)
            + b_n
        )

        # New hidden state
        h = (1 - z) * n + z * h

        cache.append({
            "x": x,
            "previous_h": previous_h,
            "z": z,
            "r": r,
            "n": n
        })

    logits = W_y @ h + b_y

    probabilities = softmax(logits)

    return probabilities, cache, h

# =====================================
# 6. Cross-entropy loss
# =====================================

def calculate_loss(probabilities, target):

    return -np.log(
        probabilities[target, 0] + 1e-12
    )

# =====================================
# 7. Backpropagation Through Time
# =====================================

def backward(probabilities, target, cache, final_h):

    # Initialize gradients
    gradients = {
        "W_xz": np.zeros_like(W_xz),
        "W_hz": np.zeros_like(W_hz),
        "b_z": np.zeros_like(b_z),

        "W_xr": np.zeros_like(W_xr),
        "W_hr": np.zeros_like(W_hr),
        "b_r": np.zeros_like(b_r),

        "W_xn": np.zeros_like(W_xn),
        "W_hn": np.zeros_like(W_hn),
        "b_n": np.zeros_like(b_n),

        "W_y": np.zeros_like(W_y),
        "b_y": np.zeros_like(b_y)
    }

    # Output gradient
    dy = probabilities.copy()
    dy[target, 0] -= 1

    gradients["W_y"] = dy @ final_h.T
    gradients["b_y"] = dy

    dh = W_y.T @ dy

    # Reverse through time
    for step in reversed(cache):

        x = step["x"]
        previous_h = step["previous_h"]

        z = step["z"]
        r = step["r"]
        n = step["n"]

        # h = (1-z)*n + z*previous_h
        dn = dh * (1 - z)
        dz = dh * (previous_h - n)

        dh_previous = dh * z

        # Candidate state derivative
        da_n = dn * (1 - n ** 2)

        gradients["W_xn"] += da_n @ x.T
        gradients["W_hn"] += da_n @ (r * previous_h).T
        gradients["b_n"] += da_n

        d_rh = W_hn.T @ da_n

        # Reset gate derivative
        dr = d_rh * previous_h

        dh_previous += d_rh * r

        da_r = dr * r * (1 - r)

        gradients["W_xr"] += da_r @ x.T
        gradients["W_hr"] += da_r @ previous_h.T
        gradients["b_r"] += da_r

        dh_previous += W_hr.T @ da_r

        # Update gate derivative
        da_z = dz * z * (1 - z)

        gradients["W_xz"] += da_z @ x.T
        gradients["W_hz"] += da_z @ previous_h.T
        gradients["b_z"] += da_z

        dh_previous += W_hz.T @ da_z

        # Continue to previous time step
        dh = dh_previous

    return gradients

# =====================================
# 8. Training
# =====================================

parameters = {
    "W_xz": W_xz,
    "W_hz": W_hz,
    "b_z": b_z,

    "W_xr": W_xr,
    "W_hr": W_hr,
    "b_r": b_r,

    "W_xn": W_xn,
    "W_hn": W_hn,
    "b_n": b_n,

    "W_y": W_y,
    "b_y": b_y
}

loss_history = []

for epoch in range(epochs):

    total_loss = 0

    order = rng.permutation(len(X_train))

    for index in order:

        sequence = X_train[index]
        target = y_train[index]

        probabilities, cache, final_h = forward(sequence)

        loss = calculate_loss(
            probabilities,
            target
        )

        total_loss += loss

        gradients = backward(
            probabilities,
            target,
            cache,
            final_h
        )

        # Clip gradients
        for gradient in gradients.values():

            np.clip(
                gradient,
                -5,
                5,
                out=gradient
            )

        # Update all parameters
        for name in parameters:

            parameters[name] -= (
                learning_rate * gradients[name]
            )

    average_loss = total_loss / len(X_train)

    loss_history.append(average_loss)

    if (epoch + 1) % 10 == 0:

        print(
            f"Epoch {epoch + 1}/{epochs} "
            f"| Loss: {average_loss:.4f}"
        )

# =====================================
# 9. Prediction
# =====================================

def predict(sequence):

    probabilities, _, _ = forward(sequence)

    predicted_class = int(np.argmax(probabilities))

    return predicted_class, probabilities.flatten()

# =====================================
# 10. Evaluation
# =====================================

predictions = []

for sequence in X_test:

    prediction, probabilities = predict(sequence)

    predictions.append(prediction)

predictions = np.array(predictions)

accuracy = np.mean(predictions == y_test)

print("\nTest accuracy:", round(accuracy * 100, 2), "%")

# =====================================
# 11. Example prediction
# =====================================

example = np.array([
    [0.8],
    [0.9],
    [0.7],
    [0.8],
    [0.9]
])

prediction, probabilities = predict(example)

print("\nExample sequence:", example.flatten())
print("Predicted class:", prediction)
print("Probabilities:", probabilities)

# =====================================
# 12. Save model and results
# =====================================

np.savez(
    OUTPUT_DIR / "gru_model.npz",
    **parameters
)

np.savetxt(
    OUTPUT_DIR / "training_loss.csv",
    np.array(loss_history),
    delimiter=",",
    header="loss",
    comments=""
)

np.savetxt(
    OUTPUT_DIR / "test_predictions.csv",
    np.column_stack((y_test, predictions)),
    delimiter=",",
    header="actual,predicted",
    comments="",
    fmt="%d"
)

print("\nGRU model and results saved successfully.")