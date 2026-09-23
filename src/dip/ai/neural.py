from __future__ import annotations

import math
import random
from typing import Any


def _sigmoid(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-max(-30.0, min(30.0, value))))


class NeuralNetwork:
    """Small dependency-free multilayer perceptron with backpropagation."""

    def __init__(self, layers: list[int], seed: int = 7):
        if len(layers) < 2 or any(size < 1 for size in layers):
            raise ValueError("layers must contain at least input and output sizes")
        self.layers = layers
        generator = random.Random(seed)
        self.weights = [
            [[generator.uniform(-1, 1) / math.sqrt(source) for _ in range(source)]
             for _ in range(target)]
            for source, target in zip(layers, layers[1:])
        ]
        self.biases = [[0.0] * target for target in layers[1:]]

    def predict(self, inputs: list[float]) -> list[float]:
        activations = self._forward(inputs)
        return activations[-1]

    def fit(self, inputs: list[list[float]], targets: list[list[float]], epochs: int = 2000,
            learning_rate: float = 0.5) -> dict[str, float]:
        if len(inputs) != len(targets) or not inputs:
            raise ValueError("inputs and targets must be nonempty and aligned")
        if any(len(row) != self.layers[0] for row in inputs):
            raise ValueError("input width does not match the network")
        if any(len(row) != self.layers[-1] for row in targets):
            raise ValueError("target width does not match the network")
        loss = 0.0
        for _ in range(epochs):
            loss = 0.0
            for row, expected in zip(inputs, targets):
                activations = self._forward(row)
                output = activations[-1]
                loss += sum((actual - wanted) ** 2 for actual, wanted in zip(output, expected))
                deltas = [[(actual - wanted) * actual * (1 - actual)
                           for actual, wanted in zip(output, expected)]]
                for layer in range(len(self.weights) - 1, 0, -1):
                    current = activations[layer]
                    downstream = deltas[0]
                    delta = []
                    for source_index, activation in enumerate(current):
                        error = sum(self.weights[layer][target_index][source_index] * downstream[target_index]
                                    for target_index in range(len(downstream)))
                        delta.append(error * activation * (1 - activation))
                    deltas.insert(0, delta)
                for layer, delta in enumerate(deltas):
                    previous = activations[layer]
                    for target_index, error in enumerate(delta):
                        self.biases[layer][target_index] -= learning_rate * error
                        for source_index, activation in enumerate(previous):
                            self.weights[layer][target_index][source_index] -= learning_rate * error * activation
        return {"loss": loss / len(inputs)}

    def artifact(self) -> dict[str, Any]:
        return {"layers": self.layers, "weights": self.weights, "biases": self.biases,
                "activation": "sigmoid"}

    def _forward(self, inputs: list[float]) -> list[list[float]]:
        if len(inputs) != self.layers[0]:
            raise ValueError("input width does not match the network")
        activations = [[float(value) for value in inputs]]
        for weights, biases in zip(self.weights, self.biases):
            activations.append([
                _sigmoid(bias + sum(weight * value for weight, value in zip(neuron, activations[-1])))
                for neuron, bias in zip(weights, biases)
            ])
        return activations
