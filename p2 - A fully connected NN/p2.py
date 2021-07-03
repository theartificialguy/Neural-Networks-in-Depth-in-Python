inputs = [1.4, 7.2, 4.5]
n1_weights = [0.35, 0.25, 0.71]
n2_weights = [0.96, 0.23, 0.56]
n3_weights = [0.37, 0.32, 0.26]
n4_weights = [0.88, 0.13, 0.42]
biases = [1.5, 2.1, 0.6, 1.7]

outputs = [
	inputs[0]*n1_weights[0]+inputs[1]*n1_weights[1]+inputs[2]*n1_weights[2] + biases[0],
	inputs[0]*n2_weights[0]+inputs[1]*n2_weights[1]+inputs[2]*n2_weights[2] + biases[1],
	inputs[0]*n3_weights[0]+inputs[1]*n3_weights[1]+inputs[2]*n3_weights[2] + biases[2],
	inputs[0]*n4_weights[0]+inputs[1]*n4_weights[1]+inputs[2]*n4_weights[2] + biases[3],
]

print(outputs)

############################################# WITH LOOPS #############################################

inputs = [1.4, 7.2, 4.5]
weights = [[0.35, 0.25, 0.71],
			[0.96, 0.23, 0.56],
			[0.37, 0.32, 0.26],
			[0.88, 0.13, 0.42]]
biases = [1.5, 2.1, 0.6, 1.7]

num_neurons = len(weights)
num_prev_output = len(inputs)

outputs = []
for i in range(num_neurons):
	current_neuron_output = 0
	for j in range(num_prev_output):
		# single neuron output
		current_neuron_output += inputs[j]*weights[i][j]
	current_neuron_output += biases[i]
	outputs.append(current_neuron_output)

print(outputs)