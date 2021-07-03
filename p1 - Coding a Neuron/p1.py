inputs = [1, 1.5, 2.9]
weights = [0.5, 0.8, 0.2]
bias = 1.5

output = round(inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias, 2)
print(output)