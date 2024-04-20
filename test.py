import numpy as np
from sklearn.datasets import load_iris
import random


class MLP:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # initialize weights matrix and biases
        self.W_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.b_input_hidden = np.zeros((1, self.hidden_size))
        self.W_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        self.b_hidden_output = np.zeros((1, self.output_size))

        # auxiliar functions

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def d_sigmoid(self, x):
        return x * (1 - x)

    def forward(self, input_data):
        hidden_layer_input = np.dot(input_data, self.W_input_hidden) + self.b_input_hidden
        hidden_layer_output = self.sigmoid(hidden_layer_input)
        output_layer_input = np.dot(hidden_layer_output, self.W_hidden_output) + self.b_hidden_output
        output = self.sigmoid(output_layer_input)

        return hidden_layer_output, output

    def backward(self, input_data, target, hidden_output, output, lr=0.2):

        # Backward propagation
        output_error = target - output
        output_grad = output_error * self.d_sigmoid(output)

        hidden_error = np.dot(output_grad, self.W_hidden_output.T)
        hidden_grad = hidden_error * self.d_sigmoid(hidden_output)

        # Update weights and biases using gradient descent
        self.W_hidden_output = self.W_hidden_output + np.dot(hidden_output.T, output_grad)*lr
        self.b_hidden_output = self.b_hidden_output + np.sum(output_grad)*lr

        self.W_input_hidden = self.W_input_hidden + np.dot(input_data.T, hidden_grad)*lr
        self.b_input_hidden = self.b_input_hidden + np.sum(hidden_grad, axis=0, keepdims=True)*lr

    def train(self, input_data, target, epochs=1000):
        for epoch in range(epochs):
            hidden_output, output = self.forward(input_data)
            self.backward(input_data, target, hidden_output, output)
