import numpy as np
from pathlib import Path

# -------------------------------
# 1. Project paths
# -------------------------------

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

rng = np.random.default_rng(42)

# -------------------------------
# 2. Generate dataset
# -------------------------------

def create_dataset(samples=1000, sequence_length=5):

    X = rng.uniform(
        0,
        10,
        size=(samples, sequence_length, 1)
    )

    averages = X.mean(axis=(1, 2))

    y = (averages >= 5).astype(int)

    return X, y


X, y = create_dataset()

# Split dataset
split = int(0.8 * len(X))

X_train = X[:split]
y_train = y[:split]

X_test = X[split:]
y_test = y[split:]

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)

# -------------------------------
# 3. Model configuration
# -------------------------------

input_size = 1
hidden_size = 8
output_size = 2

learning_rate = 0.01
epochs = 100

# Initialize weights
W_xh = rng.normal(
    0, 0.1,
    (hidden_size, input_size)
)

W_hh = rng.normal(
    0, 0.1,
    (hidden_size, hidden_size)
)

W_hy = rng.normal(
    0, 0.1,
    (output_size, hidden_size)
)

b_h = np.zeros((hidden_size, 1))
b_y = np.zeros((output_size, 1))

# -------------------------------
# 4. Activation functions
# -------------------------------

def softmax(values):

    values = values - np.max(values)

    exp_values = np.exp(values)

    return exp_values / np.sum(exp_values)


# -------------------------------
# 5. Forward propagation
# -------------------------------

def forward(sequence):

    hidden_state = np.zeros((hidden_size, 1))

    hidden_states = [hidden_state]
    inputs = []

    for value in sequence:

        x = np.array([[value]])

        hidden_state = np.tanh(
            W_xh @ x
            + W_hh @ hidden_state
            + b_h
        )

        inputs.append(x)
        hidden_states.append(hidden_state)

    logits = W_hy @ hidden_state + b_y

    probabilities = softmax(logits)

    cache = (inputs, hidden_states)

    return probabilities, cache


# -------------------------------
# 6. Training
# -------------------------------

loss_history = []

for epoch in range(epochs):

    total_loss = 0

    order = rng.permutation(len(X_train))

    for index in order:

        sequence = X_train[index]
        target = y_train[index]

        probabilities, cache = forward(sequence)

        inputs, hidden_states = cache

        # Cross-entropy loss
        loss = -np.log(
            probabilities[target, 0] + 1e-12
        )

        total_loss += loss

        # Output gradient
        dy = probabilities.copy()

        dy[target, 0] -= 1

        dW_hy = dy @ hidden_states[-1].T
        db_y_grad = dy

        # Backpropagation Through Time
        dh = W_hy.T @ dy

        dW_xh = np.zeros_like(W_xh)
        dW_hh = np.zeros_like(W_hh)
        db_h_grad = np.zeros_like(b_h)

        for t in reversed(range(len(inputs))):

            current_hidden = hidden_states[t + 1]
            previous_hidden = hidden_states[t]

            dtanh = dh * (1 - current_hidden ** 2)

            dW_xh += dtanh @ inputs[t].T
            dW_hh += dtanh @ previous_hidden.T

            db_h_grad += dtanh

            dh = W_hh.T @ dtanh

        # Gradient clipping
        gradients = [
            dW_xh,
            dW_hh,
            dW_hy,
            db_h_grad,
            db_y_grad
        ]

        for gradient in gradients:
            np.clip(
                gradient,
                -5,
                5,
                out=gradient
            )

        # Update parameters
        W_xh -= learning_rate * dW_xh
        W_hh -= learning_rate * dW_hh
        W_hy -= learning_rate * dW_hy

        b_h -= learning_rate * db_h_grad
        b_y -= learning_rate * db_y_grad

    average_loss = total_loss / len(X_train)

    loss_history.append(average_loss)

    if (epoch + 1) % 10 == 0:

        print(
            f"Epoch {epoch + 1}/{epochs} "
            f"| Loss: {average_loss:.4f}"
        )


# -------------------------------
# 7. Prediction
# -------------------------------

def predict(sequence):

    probabilities, _ = forward(sequence)

    predicted_class = np.argmax(probabilities)

    return predicted_class, probabilities.flatten()


# -------------------------------
# 8. Evaluation
# -------------------------------

correct = 0

predictions = []

for index in range(len(X_test)):

    prediction, probabilities = predict(X_test[index])

    predictions.append(prediction)

    if prediction == y_test[index]:
        correct += 1

accuracy = correct / len(X_test)

print("\nTest accuracy:", round(accuracy * 100, 2), "%")


# -------------------------------
# 9. Example prediction
# -------------------------------

example = np.array([
    [8.0],
    [7.0],
    [9.0],
    [8.0],
    [9.0]
])

prediction, probabilities = predict(example)

print("\nExample sequence:", example.flatten())
print("Predicted class:", prediction)
print("Class probabilities:", probabilities)


# -------------------------------
# 10. Save results
# -------------------------------

np.savez(
    OUTPUT_DIR / "rnn_model.npz",
    W_xh=W_xh,
    W_hh=W_hh,
    W_hy=W_hy,
    b_h=b_h,
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

print("\nRNN model and results saved successfully.")