import json
import random
import os

class MathFunctions:
    def __init__(self, weight=None, bias=None):
        # Use provided values (from JSON) or generate random ones
        self.weight = weight if weight is not None else random.uniform(-2, 2)
        self.bias = bias if bias is not None else random.uniform(-5, 5)
        self.last_weight = self.weight
        self.last_bias = self.bias

    def return_mod(self, prev):
        # Force integer output as requested
        return int(prev * self.weight + self.bias)

    def tweak(self, success_score):
        """
        success_score: > 0 for good, < 0 for bad.
        If bad, revert to previous state before nudging again.
        """
        if success_score < 0:
            self.weight = self.last_weight
            self.bias = self.last_bias
        
        self.last_weight = self.weight
        self.last_bias = self.bias
        
        # Nudge the weights slightly
        self.weight += random.uniform(-0.1, 0.1)
        self.bias += random.uniform(-0.5, 0.5)

    def to_dict(self):
        return {"weight": self.weight, "bias": self.bias}

class Node:
    def __init__(self, node_id, destinations=None, logic=None):
        self.node_id = node_id
        self.destinations = destinations if destinations else []
        self.logic = logic if logic else MathFunctions()

    def process(self, input_val):
        output = self.logic.return_mod(input_val)
        # If no destinations, it's an output node; return the value
        if not self.destinations:
            return output
        # Pass to the first destination for this simple chain
        return self.destinations[0].process(output)

    def learn(self, score):
        self.logic.tweak(score)
        for dest in self.destinations:
            dest.learn(score)

class NeuralNet:
    def __init__(self, filename="save.json"):
        self.filename = filename
        self.nodes = self.load()

    def save(self):
        data = {str(n.node_id): n.logic.to_dict() for n in self.nodes}
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Network saved.")

    def load(self):
        if not os.path.exists(self.filename):
            print("No save found. Creating new network...")
            # Create a simple 3-node chain by default
            n3 = Node(2)
            n2 = Node(1, [n3])
            n1 = Node(0, [n2])
            return [n1, n2, n3]

        with open(self.filename, "r") as f:
            data = json.load(f)
        
        # Reconstruct nodes from JSON
        new_nodes = []
        for i in range(len(data)):
            node_data = data[str(i)]
            logic = MathFunctions(weight=node_data['weight'], bias=node_data['bias'])
            new_nodes.append(Node(i, logic=logic))
        
        # Link them back together in a chain
        for i in range(len(new_nodes) - 1):
            new_nodes[i].destinations = [new_nodes[i+1]]
            
        print("Network loaded.")
        return new_nodes

    def run(self, val):
        return self.nodes[0].process(val)

    def train(self, score):
        self.nodes[0].learn(score)
        self.save()

# --- Main Program Loop ---
net = NeuralNet()

while True:
    user_val = input("\nEnter an integer to process (or 'q' to quit): ")
    if user_val.lower() == 'q':
        break
    
    try:
        val = int(user_val)
        result = net.run(val)
        print(f"Neural Net Output: {result}")
        
        feedback = input("Was this good? (y/n): ").lower()
        score = 1 if feedback == 'y' else -1
        
        net.train(score)
        
    except ValueError:
        print("Please enter a valid integer.")
