from pso import particleSwarmOptimization
from visualize2dPSOResults import visualize2dPSOHistory

def banana(position, a=1, b=100):
    x, y = position
    return (a - x)**2 + b * (y - x**2)**2

iterations=500
lowerBound=-2
upperBound=2
swarmSize=20

globalBest, history = particleSwarmOptimization(fitness=banana, lowerBound=lowerBound, upperBound=upperBound, swarmSize=swarmSize, maxIterations=iterations) 
visualize2dPSOHistory(functionName="banana",history=history, lowerBound=lowerBound, upperBound=upperBound, fitness=banana, iterations=iterations, optimalSolution=[1,1])