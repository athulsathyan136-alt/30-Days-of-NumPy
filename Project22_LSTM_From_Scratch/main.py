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
# 2. Create synthetic sequence dataset
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

# Each gate has its own weights and bias.
# Gate order: input, forget, output, candidate

W_x = rng.normal(
    0, 0.1,
    (4 * hidden_size, input_size)
)

W_h = rng.normal(
    0, 0.1,
    (4 * hidden_size, hidden_size)
)

b = np.zeros((4 * hidden_size, 1))

# Output layer
W_y = rng.normal(
    0, 0.1,
    (output_size, hidden_size)
)

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
# 5. LSTM forward propagation
# =====================================

def forward(sequence):

    h = np.zeros((hidden_size, 1))
    c = np.zeros((hidden_size, 1))

    cache = []

    for value in sequence:

        x = np.array([[value]])

        previous_h = h.copy()
        previous_c = c.copy()

        gates = W_x @ x + W_h @ h + b

        # Split gate calculations
        z_i, z_f, z_o, z_g = np.split(
            gates,
            4,
            axis=0
        )

        # Input gate
        i = sigmoid(z_i)

        # Forget gate
        f = sigmoid(z_f)

        # Output gate
        o = sigmoid(z_o)

        # Candidate memory
        g = np.tanh(z_g)

        # Update cell state
        c = f * c + i * g

        # Update hidden state
        tanh_c = np.tanh(c)

        h = o * tanh_c

        cache.append({
            "x": x,
            "previous_h": previous_h,
            "previous_c": previous_c,
            "i": i,
            "f": f,
            "o": o,
            "g": g,
            "c": c.copy(),
            "tanh_c": tanh_c
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

def backward(probabilities, target, cache):

    dW_x = np.zeros_like(W_x)
    dW_h = np.zeros_like(W_h)
    db_grad = np.zeros_like(b)

    dW_y = np.zeros_like(W_y)
    db_y_grad = np.zeros_like(b_y)

    # Output-layer gradient
    dy = probabilities.copy()
    dy[target, 0] -= 1

    final_h = cache[-1]["o"] * cache[-1]["tanh_c"]

    dW_y = dy @ final_h.T
    db_y_grad = dy

    dh = W_y.T @ dy
    dc = np.zeros((hidden_size, 1))

    # Move backward through time
    for step in reversed(cache):

        i = step["i"]
        f = step["f"]
        o = step["o"]
        g = step["g"]

        current_c = step["c"]
        previous_c = step["previous_c"]
        previous_h = step["previous_h"]

        tanh_c = step["tanh_c"]

        # Output gate gradient
        do = dh * tanh_c

        # Cell state gradient
        dc = dc + dh * o * (1 - tanh_c ** 2)

        # Input, forget and candidate gradients
        di = dc * g
        df = dc * previous_c
        dg = dc * i

        # Derivatives through activations
        dz_i = di * i * (1 - i)
        dz_f = df * f * (1 - f)
        dz_o = do * o * (1 - o)
        dz_g = dg * (1 - g ** 2)

        # Combine gate gradients
        dz = np.vstack([
            dz_i,
            dz_f,
            dz_o,
            dz_g
        ])

        # Parameter gradients
        dW_x += dz @ step["x"].T
        dW_h += dz @ previous_h.T
        db_grad += dz

        # Pass gradients to previous time step
        dh = W_h.T @ dz

        dc = dc * f

    return [
        dW_x,
        dW_h,
        db_grad,
        dW_y,
        db_y_grad
    ]


# =====================================
# 8. Training
# =====================================

loss_history = []

for epoch in range(epochs):

    total_loss = 0

    order = rng.permutation(len(X_train))

    for index in order:

        sequence = X_train[index]
        target = y_train[index]

        probabilities, cache, _ = forward(sequence)

        loss = calculate_loss(
            probabilities,
            target
        )

        total_loss += loss

        gradients = backward(
            probabilities,
            target,
            cache
        )

        dW_x, dW_h, db_grad, dW_y, db_y_grad = gradients

        # Gradient clipping
        for gradient in gradients:
            np.clip(
                gradient,
                -5,
                5,
                out=gradient
            )

        # Update weights
        W_x[:] -= learning_rate * dW_x
        W_h[:] -= learning_rate * dW_h
        b[:] -= learning_rate * db_grad

        W_y[:] -= learning_rate * dW_y
        b_y[:] -= learning_rate * db_y_grad

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
# 10. Model evaluation
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
    OUTPUT_DIR / "lstm_model.npz",
    W_x=W_x,
    W_h=W_h,
    b=b,
    W_y=W_y,
    b_y=b_y
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

print("\nLSTM model and results saved successfully.")