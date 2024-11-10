from pso import particleSwarmOptimization
from visualize3dPSOResults import visualize3dPSOHistory
import numpy as np

schwefel3DGlobalMin = [420.9687,420.9687,420.9687]
def schwefel3D(position):
    return 418.9829 * 3 - np.sum(position * np.sin(np.sqrt(np.abs(position))))

iterations=300
lowerBound=-500
upperBound=500
swarmSize=100

globalBest, history = particleSwarmOptimization(fitness=schwefel3D, dimension=3, lowerBound=lowerBound, upperBound=upperBound, swarmSize=swarmSize, maxIterations=iterations)
visualize3dPSOHistory(functionName="3d_schwefel_function", history=history, lowerBound=lowerBound, upperBound=upperBound, fitness=schwefel3D, iterations=iterations, optimalSolution=schwefel3DGlobalMin)