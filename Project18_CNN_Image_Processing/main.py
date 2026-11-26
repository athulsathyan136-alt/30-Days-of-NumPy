
import numpy as np

# =========================================
# 1. CREATE SYNTHETIC IMAGES
# =========================================

# Image A: vertical white line
vertical_image = np.zeros((8, 8))
vertical_image[:, 3:5] = 1

# Image B: horizontal white line
horizontal_image = np.zeros((8, 8))
horizontal_image[3:5, :] = 1

# Image C: diagonal pattern
diagonal_image = np.zeros((8, 8))

for i in range(8):
    diagonal_image[i, i] = 1

images = [
    vertical_image,
    horizontal_image,
    diagonal_image
]

labels = ["Vertical", "Horizontal", "Diagonal"]

# =========================================
# 2. DEFINE CONVOLUTION FUNCTION
# =========================================

def convolution(image, kernel):

    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1

    output = np.zeros((output_height, output_width))

    for i in range(output_height):
        for j in range(output_width):

            region = image[
                i:i + kernel_height,
                j:j + kernel_width
            ]

            output[i, j] = np.sum(region * kernel)

    return output


# =========================================
# 3. DEFINE EDGE DETECTION FILTERS
# =========================================

vertical_filter = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

horizontal_filter = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

diagonal_filter = np.array([
    [ 0,  1,  1],
    [-1,  0,  1],
    [-1, -1,  0]
])

filters = [
    vertical_filter,
    horizontal_filter,
    diagonal_filter
]

# =========================================
# 4. APPLY CONVOLUTION AND RELU
# =========================================

feature_maps = []

for image in images:

    image_feature_maps = []

    for kernel in filters:

        result = convolution(image, kernel)

        # ReLU activation
        activated = np.maximum(0, result)

        image_feature_maps.append(activated)

    feature_maps.append(image_feature_maps)


# =========================================
# 5. MAX POOLING
# =========================================

def max_pooling(feature_map):

    height, width = feature_map.shape

    pooled_height = height // 2
    pooled_width = width // 2

    pooled = np.zeros((pooled_height, pooled_width))

    for i in range(pooled_height):
        for j in range(pooled_width):

            region = feature_map[
                i * 2:i * 2 + 2,
                j * 2:j * 2 + 2
            ]

            pooled[i, j] = np.max(region)

    return pooled


# =========================================
# 6. EXTRACT FEATURES
# =========================================

all_features = []

for image_feature_maps in feature_maps:

    pooled_features = []

    for feature_map in image_feature_maps:

        pooled = max_pooling(feature_map)

        pooled_features.append(pooled.flatten())

    combined_features = np.concatenate(
        pooled_features
    )

    all_features.append(combined_features)

X = np.array(all_features)

print("\n===== CNN FEATURE EXTRACTION =====")

print("Feature matrix shape:", X.shape)


# =========================================
# 7. SIMPLE RULE-BASED CLASSIFICATION
# =========================================

# Each synthetic image has a known category.
# This section demonstrates selecting the strongest
# filter response, not training a CNN classifier.

filter_scores = []

for image_feature_maps in feature_maps:

    scores = np.array([
        np.sum(feature_map)
        for feature_map in image_feature_maps
    ])

    filter_scores.append(scores)

filter_scores = np.array(filter_scores)

predictions = np.argmax(
    filter_scores,
    axis=1
)

print("\n===== IMAGE CLASSIFICATION =====")

for i in range(len(images)):

    predicted_label = labels[predictions[i]]

    print(
        "Image:", labels[i],
        "| Predicted:", predicted_label
    )


# =========================================
# 8. SAVE OUTPUTS
# =========================================

np.save(
    "outputs/extracted_features.npy",
    X
)

np.save(
    "outputs/filter_scores.npy",
    filter_scores
)

print("\nFeature extraction completed!")
print("Output files saved successfully!")
