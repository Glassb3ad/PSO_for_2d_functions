from pso import particleSwarmOptimization
from visualize1dPSOResults import visualize1dPSOHistory
import numpy as np

def schwefel1D(position):
    x = position[0]
    return 418.9829 - x * np.sin(np.sqrt(abs(x)))

iterations=200
lowerBound=-500
upperBound=500
swarmSize=20

globalBest, history = particleSwarmOptimization(fitness=schwefel1D, dimension=1, lowerBound=lowerBound, upperBound=upperBound, swarmSize=swarmSize, maxIterations=iterations) 
print(globalBest.shape[0])
print(globalBest)
visualize1dPSOHistory(filename="1d_schwefel_function_PSO_optimization",history=history, fitness=schwefel1D, lowerBound=lowerBound, upperBound=upperBound, iterations=iterations)