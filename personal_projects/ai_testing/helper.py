import numpy as np
import matplotlib.pyplot as plt
import json
import os

class OptimizedNet:
    def __init__(self, size=3, filename="save.json"):
        self.filename = filename
        self.size = size
        # Use NumPy arrays for O(1) vectorized math instead of recursive objects
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.weights = np.array([data[k]['weight'] for k in sorted(data.keys())])
                self.biases = np.array([data[k]['bias'] for k in sorted(data.keys())])
        else:
            self.weights = np.random.uniform(-2, 2, size)
            self.biases = np.random.uniform(-5, 5, size)
        
        self.last_weights = self.weights.copy()
        self.last_biases = self.biases.copy()

    def run(self, val):
        # Vectorized forward pass: result = (...((val * w1 + b1) * w2 + b2)...)
        res = val
        if res>1000000000000000000:
            print("hit top")
            return 1000000000000000000
        for w, b in zip(self.weights, self.biases):
            res = int(res * w + b)
        return res

    def train(self, score, rate_of_change=0.1):
        # Logic: Revert if bad, save if good
        if score < 0:
            self.weights[:] = self.last_weights
            self.biases[:] = self.last_biases
        else:
            self.last_weights[:] = self.weights
            self.last_biases[:] = self.biases

        # Batch update weights and biases using noise scaled by score
        magnitude = abs(score) * rate_of_change
        self.weights += np.random.uniform(-0.1, 0.1, self.size) * magnitude
        self.biases += np.random.uniform(-0.5, 0.5, self.size) * magnitude

    def save(self):
        data = {i: {"weight": w, "bias": b} for i, (w, b) in enumerate(zip(self.weights, self.biases))}
        with open(self.filename, "w") as f:
            json.dump(data, f)

# --- Execution ---
net = OptimizedNet()
history = []

# Optimization: Removed print() and save() from the loop. 
# Printing to console and writing to SSD are the slowest operations in Python.
for x in range(5000):
    val = np.random.randint(1, 10)
    result = net.run(val)
    history.append(result)
    print(f"{x}:{result}")
    net.train(result)
    
# Save once at the end
net.save()

plt.plot(history)
plt.title("Optimized Network Output")
plt.show()
