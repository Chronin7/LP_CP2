from helper import NeuralNet

# Define the network structure: [input_size, hidden1_size, ..., output_size]
# For example, 2 inputs, 3 hidden nodes, 1 output
layers = [2, 3, 1]
net = NeuralNet(layers)

print("Neural Network initialized.")
print(f"Input layer: {len(net.layers[0])} nodes")
print(f"Output layer: {len(net.layers[-1])} nodes")

while True:
    try:
        user_input = input("\nEnter inputs separated by spaces (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        
        inputs = [float(x) for x in user_input.split()]
        if len(inputs) != layers[0]:
            print(f"Please enter exactly {layers[0]} inputs.")
            continue
        
        outputs = net.run(inputs)
        print(f"Outputs: {outputs}")
        
        score_input = input("Enter training score (float, higher = better): ")
        score = float(score_input)
        
        net.train(score)
        print("Network trained and saved.")
        
    except ValueError as e:
        print(f"Invalid input: {e}")
    except KeyboardInterrupt:
        break

print("Goodbye!")