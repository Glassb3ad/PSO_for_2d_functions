from pso import particleSwarmOptimization
from visualize2dPSOResults import visualize2dPSOHistory
import numpy as np

def schwefel2D(position):
    x, y = position
    return 418.9829 * 2 - (x * np.sin(np.sqrt(abs(x))) + y * np.sin(np.sqrt(abs(y))))

iterations=500
lowerBound=-500
upperBound=500
swarmSize=15

globalBest, history = particleSwarmOptimization(fitness=schwefel2D, lowerBound=lowerBound, upperBound=upperBound, swarmSize=swarmSize, maxIterations=iterations) 
visualize2dPSOHistory(filename="schwefel_function_PSO_optimization",history=history, lowerBound=lowerBound, upperBound=upperBound, fitness=schwefel2D, iterations=iterations)