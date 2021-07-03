################################################## NEURON #################################################

import numpy as np

inputs = [1, 1.5, 2.9]
weights = [0.5, 0.8, 0.2]
bias = 1.5

outputs = np.dot(weights, inputs) + bias
print(outputs)

################################################## LAYER #################################################

inputs = [1.4, 7.2, 4.5]
weights = [[0.35, 0.25, 0.71],
			[0.96, 0.23, 0.56],
			[0.37, 0.32, 0.26],
			[0.88, 0.13, 0.42]]
biases = [1.5, 2.1, 0.6, 1.7]
'''
shapes should be same, i.e. elements between those where dot product will take place for eg:
weights[i]*inputs, both has same shape i.e. 1x3 and 1x3
'''
outputs = np.dot(weights, inputs) + biases
'''
insides:

outputs = [np.dot(weights[0], inputs), np.dot(weights[1], inputs), np.dot(weights[2], inputs)]

we passed weights as our first argument in np.dot() because we wanted the output shape to be
of 4 neuron output, as np.dot() performs operation treating the matrix 1 vector list at a time
and multiplying it with input.
'''
print(outputs)