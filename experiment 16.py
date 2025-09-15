import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([
    [0],
    [1],
    [1],
    [0]
])
np.random.seed(1)
input_layer_size = 2
hidden_layer_size = 2
output_layer_size = 1
W1 = 2 * np.random.random((input_layer_size, hidden_layer_size)) - 1
b1 = np.zeros((1, hidden_layer_size))
W2 = 2 * np.random.random((hidden_layer_size, output_layer_size)) - 1
b2 = np.zeros((1, output_layer_size))
learning_rate = 0.5
epochs = 10000
for epoch in range(epochs):
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    output = sigmoid(z2)
    error = y - output
    d_output = error * sigmoid_derivative(output)
    d_hidden = d_output.dot(W2.T) * sigmoid_derivative(a1)
    W2 += a1.T.dot(d_output) * learning_rate
    b2 += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    W1 += X.T.dot(d_hidden) * learning_rate
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate
print("Final Output after training:")
print(output.round(3))
