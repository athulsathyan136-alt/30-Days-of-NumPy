
import numpy as np

# ==========================================
# 1. CONFIGURATION
# ==========================================

rng = np.random.default_rng(42)

vocabulary = [
    "AI", "learns", "from", "data",
    "machine", "models", "and", "patterns"
]

vocab_size = len(vocabulary)
sequence_length = 4
embedding_dim = 8
num_heads = 2
head_dim = embedding_dim // num_heads
epsilon = 1e-5

token_to_id = {
    word: i for i, word in enumerate(vocabulary)
}

# ==========================================
# 2. TOKENIZATION
# ==========================================

sentence = ["AI", "learns", "from", "data"]

token_ids = np.array([
    token_to_id[word] for word in sentence
])

print("\n===== TOKENIZATION =====")
print("Tokens:", sentence)
print("Token IDs:", token_ids)

# ==========================================
# 3. TOKEN EMBEDDINGS
# ==========================================

embedding_table = rng.normal(
    0, 0.1,
    (vocab_size, embedding_dim)
)

X = embedding_table[token_ids]

print("\n===== TOKEN EMBEDDINGS =====")
print("Embedding shape:", X.shape)

# ==========================================
# 4. POSITIONAL ENCODING
# ==========================================

def positional_encoding(length, dimension):

    positions = np.arange(length)[:, None]

    dimensions = np.arange(dimension)[None, :]

    angles = positions / np.power(
        10000,
        (2 * (dimensions // 2)) / dimension
    )

    encoding = np.zeros((length, dimension))

    encoding[:, 0::2] = np.sin(angles[:, 0::2])
    encoding[:, 1::2] = np.cos(angles[:, 1::2])

    return encoding


position_values = positional_encoding(
    sequence_length,
    embedding_dim
)

X = X + position_values

# ==========================================
# 5. INITIALIZE ATTENTION WEIGHTS
# ==========================================

Wq = rng.normal(
    0, 0.1,
    (embedding_dim, embedding_dim)
)

Wk = rng.normal(
    0, 0.1,
    (embedding_dim, embedding_dim)
)

Wv = rng.normal(
    0, 0.1,
    (embedding_dim, embedding_dim)
)

Wo = rng.normal(
    0, 0.1,
    (embedding_dim, embedding_dim)
)

# ==========================================
# 6. SOFTMAX FUNCTION
# ==========================================

def softmax(x, axis=-1):

    shifted = x - np.max(
        x,
        axis=axis,
        keepdims=True
    )

    exp_values = np.exp(shifted)

    return exp_values / np.sum(
        exp_values,
        axis=axis,
        keepdims=True
    )


# ==========================================
# 7. LAYER NORMALIZATION
# ==========================================

def layer_norm(x):

    mean = np.mean(
        x,
        axis=-1,
        keepdims=True
    )

    variance = np.var(
        x,
        axis=-1,
        keepdims=True
    )

    return (
        (x - mean)
        / np.sqrt(variance + epsilon)
    )


# ==========================================
# 8. MULTI-HEAD SELF-ATTENTION
# ==========================================

Q = np.dot(X, Wq)
K = np.dot(X, Wk)
V = np.dot(X, Wv)

# Split projections into attention heads
Q_heads = Q.reshape(
    sequence_length,
    num_heads,
    head_dim
).transpose(1, 0, 2)

K_heads = K.reshape(
    sequence_length,
    num_heads,
    head_dim
).transpose(1, 0, 2)

V_heads = V.reshape(
    sequence_length,
    num_heads,
    head_dim
).transpose(1, 0, 2)

# Causal mask:
# Each token can only attend to itself
# and previous tokens.

causal_mask = np.triu(
    np.ones((sequence_length, sequence_length)),
    k=1
).astype(bool)

head_outputs = []
attention_maps = []

for head in range(num_heads):

    scores = np.dot(
        Q_heads[head],
        K_heads[head].T
    ) / np.sqrt(head_dim)

    scores = np.where(
        causal_mask,
        -1e9,
        scores
    )

    attention_weights = softmax(scores)

    head_output = np.dot(
        attention_weights,
        V_heads[head]
    )

    head_outputs.append(head_output)
    attention_maps.append(attention_weights)

# Combine attention heads
combined = np.concatenate(
    head_outputs,
    axis=1
)

attention_output = np.dot(
    combined,
    Wo
)

# Residual connection and normalization
X = layer_norm(X + attention_output)

print("\n===== ATTENTION =====")
print("Attention output shape:", X.shape)

# ==========================================
# 9. FEED-FORWARD NETWORK
# ==========================================

W1 = rng.normal(
    0, 0.1,
    (embedding_dim, 16)
)

b1 = np.zeros((1, 16))

W2 = rng.normal(
    0, 0.1,
    (16, embedding_dim)
)

b2 = np.zeros((1, embedding_dim))

hidden = np.maximum(
    0,
    np.dot(X, W1) + b1
)

feed_forward_output = (
    np.dot(hidden, W2) + b2
)

# Residual connection and normalization
X = layer_norm(
    X + feed_forward_output
)

# ==========================================
# 10. NEXT TOKEN PREDICTION
# ==========================================

output_weights = rng.normal(
    0, 0.1,
    (embedding_dim, vocab_size)
)

output_bias = np.zeros((1, vocab_size))

last_token_representation = X[-1:]

logits = (
    np.dot(last_token_representation, output_weights)
    + output_bias
)

probabilities = softmax(logits)

predicted_token_id = np.argmax(
    probabilities,
    axis=1
)[0]

predicted_word = vocabulary[predicted_token_id]

print("\n===== NEXT TOKEN PREDICTION =====")

print("Input sentence:", " ".join(sentence))
print("Predicted next token:", predicted_word)

print("\nToken probabilities:")

for i, word in enumerate(vocabulary):

    print(
        word,
        ":",
        round(float(probabilities[0, i]), 4)
    )

# ==========================================
# 11. SAVE RESULTS
# ==========================================

np.savez(
    "outputs/transformer_results.npz",
    token_ids=token_ids,
    embeddings=X,
    attention_maps=np.array(attention_maps),
    probabilities=probabilities
)

print("\nTransformer results saved!")
