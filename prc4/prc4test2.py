import numpy as np
import pandas as pd

# Define logistic function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Define cost function
def compute_cost(X, y, theta):
    m = len(y)
    h = sigmoid(np.dot(X, theta))
    epsilon = 1e-5  # to avoid log(0)
    cost = (1 / m) * np.sum(-y * np.log(h + epsilon) - (1 - y) * np.log(1 - h + epsilon))
    return cost

# Define gradient descent function
def gradient_descent(X, y, theta, alpha, iterations):
    m = len(y)
    cost_history = np.zeros(iterations)

    for i in range(iterations):
        h = sigmoid(np.dot(X, theta))
        theta = theta - (alpha / m) * np.dot(X.T, (h - y))
        cost_history[i] = compute_cost(X, y, theta)

    return theta, cost_history

# Load data from CSV file
data = pd.read_csv('iris.csv')

# Select only the first two features and corresponding labels for binary classification
X_real = data.iloc[:, :2].values
y_real = (data.iloc[:, -1] != 0) * 1  # 0 if Iris-setosa, 1 if Iris-versicolor or Iris-virginica

# Generate random indices to select random rows from real data
np.random.seed()  # Seed without an argument will use system time
random_indices = np.random.choice(len(X_real), 100, replace=False)

# Randomly select rows from real data
X_random = X_real[random_indices]
y_random = y_real[random_indices]

# Add intercept term to X
X_random = np.hstack((np.ones((X_random.shape[0], 1)), X_random))

# Initialize parameters
theta = np.zeros(X_random.shape[1])

# Set hyperparameters
alpha = 0.01
iterations = 1000

# Run gradient descent
theta, cost_history = gradient_descent(X_random, y_random, theta, alpha, iterations)

# Predict probabilities
probabilities = sigmoid(np.dot(X_random, theta))

# Convert probabilities to binary predictions
predictions = (probabilities >= 0.5) * 1

# Calculate accuracy
accuracy = np.mean(predictions == y_random) * 100
print("Accuracy:", accuracy)
