from pso import particleSwarmOptimization
from visualizePSOResults import visualizeHistory

def banana(position, a=1, b=100):
    x, y = position
    return (a - x)**2 + b * (y - x**2)**2

iterations=1000
lowerBound=-2
upperBound=2

globalBest, history = particleSwarmOptimization(fitness=banana, lowerBound=lowerBound, upperBound=upperBound, swarmSize=100, maxIterations=iterations) 
visualizeHistory(filename="banana_function_PSO_optimization",history=history, lowerBound=lowerBound, upperBound=upperBound, fitness=banana, iterations=iterations)