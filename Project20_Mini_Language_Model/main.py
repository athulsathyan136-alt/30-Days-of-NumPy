import numpy as np
from pathlib import Path

# -------------------------------
# 1. Load training text
# -------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "corpus.txt"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

text = DATA_PATH.read_text(encoding="utf-8").lower()
text = " ".join(text.split())

if len(text) < 2:
    raise ValueError("Training text must contain at least 2 characters.")

# -------------------------------
# 2. Create vocabulary
# -------------------------------

vocabulary = sorted(set(text))

char_to_id = {
    char: index
    for index, char in enumerate(vocabulary)
}

id_to_char = {
    index: char
    for char, index in char_to_id.items()
}

vocab_size = len(vocabulary)

print("Vocabulary:", vocabulary)
print("Vocabulary size:", vocab_size)

# -------------------------------
# 3. Create training pairs
# -------------------------------

inputs = np.array([
    char_to_id[char]
    for char in text[:-1]
])

targets = np.array([
    char_to_id[char]
    for char in text[1:]
])

print("Training pairs:", len(inputs))

# -------------------------------
# 4. Initialize model
# -------------------------------

rng = np.random.default_rng(42)

weights = rng.normal(
    0,
    0.01,
    size=(vocab_size, vocab_size)
)

learning_rate = 0.1
epochs = 200

# -------------------------------
# 5. Softmax function
# -------------------------------

def softmax(values):

    values = values - np.max(values)

    exp_values = np.exp(values)

    probabilities = exp_values / np.sum(exp_values)

    return probabilities

# -------------------------------
# 6. Train model
# -------------------------------

loss_history = []

for epoch in range(epochs):

    total_loss = 0

    order = rng.permutation(len(inputs))

    for index in order:

        current_char = inputs[index]
        next_char = targets[index]

        # Predict next character
        logits = weights[current_char]

        probabilities = softmax(logits)

        # Calculate cross-entropy loss
        loss = -np.log(probabilities[next_char] + 1e-12)

        total_loss += loss

        # Calculate gradient
        gradient = probabilities.copy()

        gradient[next_char] -= 1

        # Update weights
        weights[current_char] -= learning_rate * gradient

    average_loss = total_loss / len(inputs)

    loss_history.append(average_loss)

    if (epoch + 1) % 50 == 0:

        print(
            f"Epoch {epoch + 1}/{epochs} "
            f"| Loss: {average_loss:.4f}"
        )

# -------------------------------
# 7. Generate new text
# -------------------------------

def generate_text(seed, length=100, temperature=0.8):

    if not seed:
        raise ValueError("Seed cannot be empty.")

    if temperature <= 0:
        raise ValueError("Temperature must be greater than zero.")

    if seed[-1] not in char_to_id:
        raise ValueError("Seed contains a character outside the vocabulary.")

    generated = seed

    current_char = seed[-1]

    for _ in range(length):

        current_id = char_to_id[current_char]

        logits = weights[current_id] / temperature

        probabilities = softmax(logits)

        next_id = rng.choice(
            vocab_size,
            p=probabilities
        )

        next_char = id_to_char[next_id]

        generated += next_char

        current_char = next_char

    return generated

generated_text = generate_text("h", length=150)

print("\nGenerated text:")
print(generated_text)

# -------------------------------
# 8. Save model and results
# -------------------------------

np.savez(
    OUTPUT_DIR / "language_model.npz",
    weights=weights,
    vocabulary=np.array(vocabulary)
)

np.savetxt(
    OUTPUT_DIR / "training_loss.csv",
    np.array(loss_history),
    delimiter=",",
    header="loss",
    comments=""
)

(OUTPUT_DIR / "generated_text.txt").write_text(
    generated_text,
    encoding="utf-8"
)

print("\nModel and results saved successfully.")