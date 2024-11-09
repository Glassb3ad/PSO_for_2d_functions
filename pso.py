from typing import List, Callable, Optional
import numpy as np

class Particle:
    def __init__(self, location: np.ndarray, velocity: np.ndarray, dimension:Optional[int]=2):
        self.location = location
        self.best = np.copy(location)
        self.velocity = velocity
        self.dimension = dimension
    
    def updateBest(self, f):
        self.best = min([self.location, self.best], key=f)

    def updateVelocity(self, globalBest: np.ndarray, inertia: float, cognitive: float, social: float):
        r1 = np.random.rand(self.dimension)
        r2 = np.random.rand(self.dimension)
        self.velocity = (inertia * self.velocity) + (cognitive * r1 * (self.best - self.location)) + (social * r2 * (globalBest - self.location))   
    
    def updateLocation(self, lowerBound:Optional[float]=None , upperBound:Optional[float]=None):
        self.location = self.location + self.velocity
        if(lowerBound is not None and upperBound is not None):
            for n in range(self.dimension):
                self.location[n] = np.clip(self.location[n], lowerBound, upperBound)

def calculateGlobalBest(f, curGlobal: np.ndarray, swarm: List[Particle]):
    newGlobal = curGlobal
    for particle in swarm:
        newGlobal = min([newGlobal, particle.location], key=f)
    return newGlobal

def generateInitialSwarm(n: int, lowerBound: float, upperBound: float, dimension:Optional[float]=2) -> List[Particle]:
        swarm = []
        location = np.random.uniform(low=lowerBound, high=upperBound, size=(n, dimension))
        velocity = np.random.uniform(low=lowerBound, high=upperBound, size=(n, dimension))
        for index in range(n):
            swarm.append(Particle(location[index], velocity[index], dimension))
        return swarm        

def particleSwarmOptimization(fitness: Callable, lowerBound: float, upperBound: float,  swarmSize: int, maxIterations: int, inertia: Optional[float]=0.7, cognitive: Optional[float]=2.05, social:Optional[float]=2.05, dimension:Optional[int]=2):
    swarm = generateInitialSwarm(swarmSize, lowerBound, upperBound, dimension)
    globalBest = calculateGlobalBest(fitness, swarm[0].location, swarm)
    history = []
    history.append([particle.location for particle in swarm])
    iterationCount = 1
    while iterationCount <= maxIterations:
        for particle in swarm:
            particle.updateVelocity(globalBest, inertia, cognitive, social)
            particle.updateLocation(lowerBound, upperBound)
            particle.updateBest(fitness)
        globalBest = calculateGlobalBest(fitness, globalBest, swarm)
        history.append([particle.location for particle in swarm])
        iterationCount = iterationCount + 1
    return globalBest, history
