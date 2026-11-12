import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    # Your code here
    probabilities = []
    for f in features:
        z = sum(x*w for x,w in zip(f,weights)) + bias
        probability = 1/ (1+math.exp(-z))
        probabilities.append(probability)
        mse = sum((label - probability)**2 for label, probability in zip(labels, probabilities))/ len(labels)
    return probabilities, mse