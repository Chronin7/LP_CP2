import json
import random
import os

class MathFunctions:
    def __init__(self, weights=None, bias=None):
        self.weights = weights if weights is not None else []
        self.bias = bias if bias is not None else random.uniform(-5, 5)
        self.last_weights = self.weights.copy()
        self.last_bias = self.bias

    def return_mod(self, inputs):
        if not self.weights:
            return inputs[0] if inputs else 0
        return sum(w * i for w, i in zip(self.weights, inputs)) + self.bias

    def tweak(self, success_score, learning_rate=0.1):
        if success_score < 0:
            self.weights = self.last_weights.copy()
            self.bias = self.last_bias
        
        self.last_weights = self.weights.copy()
        self.last_bias = self.bias
        
        # Nudge based on score
        direction = 1 if success_score > 0 else -1
        magnitude = abs(success_score) * learning_rate
        for i in range(len(self.weights)):
            self.weights[i] += random.uniform(-magnitude, magnitude) * direction
        self.bias += random.uniform(-magnitude * 5, magnitude * 5) * direction

    def to_dict(self):
        return {"weights": self.weights, "bias": self.bias}

class Node:
    def __init__(self, node_id, num_inputs=0, logic=None):
        self.node_id = node_id
        self.num_inputs = num_inputs
        self.logic = logic if logic else MathFunctions(weights=[random.uniform(-2, 2) for _ in range(num_inputs)] if num_inputs > 0 else [])
        self.output = 0

    def process(self, inputs):
        self.output = self.logic.return_mod(inputs)
        return self.output

    def learn(self, score):
        self.logic.tweak(score)

class NeuralNet:
    def __init__(self, layers, filename="save.json"):
        self.layers = []  # list of lists of nodes
        self.filename = filename
        self.load_or_create(layers)

    def load_or_create(self, layers):
        if not os.path.exists(self.filename):
            print("No save found. Creating new network...")
            for i, size in enumerate(layers):
                layer = []
                for j in range(size):
                    if i == 0:
                        # input layer
                        node = Node(f"{i}-{j}", num_inputs=1)
                    else:
                        prev_size = layers[i-1]
                        node = Node(f"{i}-{j}", num_inputs=prev_size)
                    layer.append(node)
                self.layers.append(layer)
        else:
            with open(self.filename, "r") as f:
                data = json.load(f)
            
            for i, size in enumerate(layers):
                layer = []
                for j in range(size):
                    key = f"{i}-{j}"
                    if key in data:
                        d = data[key]
                        weights = d.get('weights', [])
                        bias = d.get('bias', 0)
                        logic = MathFunctions(weights=weights, bias=bias)
                    else:
                        if i == 0:
                            logic = MathFunctions()
                        else:
                            prev_size = layers[i-1]
                            logic = MathFunctions(weights=[random.uniform(-2, 2) for _ in range(prev_size)])
                    node = Node(f"{i}-{j}", num_inputs=layers[i-1] if i > 0 else 1, logic=logic)
                    layer.append(node)
                self.layers.append(layer)
            print("Network loaded.")

    def save(self):
        data = {}
        for layer in self.layers:
            for node in layer:
                data[node.node_id] = node.logic.to_dict()
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Network saved.")

    def run(self, inputs):
        # inputs is list of floats (or 0/1 for bool)
        if len(inputs) != len(self.layers[0]):
            raise ValueError("Number of inputs must match input layer size")
        
        # Set input layer
        for i, val in enumerate(inputs):
            self.layers[0][i].process([val])
        
        # Process hidden and output layers
        for i in range(1, len(self.layers)):
            prev_layer = self.layers[i-1]
            prev_outputs = [node.output for node in prev_layer]
            for node in self.layers[i]:
                node.process(prev_outputs)
        
        # Return outputs as list of floats
        return [node.output for node in self.layers[-1]]

    def train(self, score):
        # score is float, higher better
        for layer in self.layers:
            for node in layer:
                node.learn(score)
        self.save()
