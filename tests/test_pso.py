# test_math_operations.py
import unittest
import numpy as np
from pso import Particle, calculateGlobalBest, generateInitialSwarm, particleSwarmOptimization

def testF(x):
    return x[0]

class TestCalculateGlobalBest(unittest.TestCase):
    def test_return_current_global_best(self):
        swarm = [Particle(np.array([2, 1]), np.array([2, 1])), Particle(np.array([3, 2]), np.array([3, 2]))]
        globalBest = calculateGlobalBest(testF, np.array([1, 1]), swarm)
        self.assertEqual(globalBest[0], 1)
        self.assertEqual(globalBest[1], 1)

    def test_return_new_global_best(self):
        swarm = [Particle(np.array([2, 2]), np.array([2, 2])), Particle(np.array([3, 2]), np.array([3, 2]))]
        globalBest = calculateGlobalBest(testF, np.array([3, 3]), swarm)
        self.assertEqual(globalBest[0], 2)
        self.assertEqual(globalBest[1], 2)

class TestGenerateInitialSwatm(unittest.TestCase):
        def test_initial_swarm_has_given_length(self):
            swarm = generateInitialSwarm(20, 2, 4)
            self.assertEqual(len(swarm), 20)

        def test_location_between_bounds(self):
            swarm = generateInitialSwarm(20, 2, 4)
            for particle in swarm:
                self.assertGreaterEqual(particle.location[0], 2)
                self.assertGreaterEqual(particle.location[1], 2)
                self.assertLessEqual(particle.location[0], 4)
                self.assertLessEqual(particle.location[1], 4)

        def test_velocity_between_bounds(self):
            swarm = generateInitialSwarm(20, 1, 2)
            for particle in swarm:
                self.assertGreaterEqual(particle.velocity[0], 1)
                self.assertGreaterEqual(particle.velocity[1], 1)
                self.assertLessEqual(particle.velocity[0], 2)
                self.assertLessEqual(particle.velocity[1], 2)

class TestParticles(unittest.TestCase):
    def test_update_location(self):
        particle = Particle(np.array([1, 1]), np.array([1, 1]))
        particle.updateLocation()
        self.assertEqual(particle.location[0], 2)
        self.assertEqual(particle.location[1], 2)

    def test_cannot_fly_over_boundary(self):
        particle = Particle(np.array([0.5, 0.5]), np.array([1, 1]))
        particle.updateLocation(0,1)
        self.assertEqual(particle.location[0], 1)
        self.assertEqual(particle.location[1], 1)

    def test_update_best_when_current_location_is_better(self):
        particle = Particle(np.array([2, 2]), np.array([1, 1]))
        particle.best = np.array([3, 3])
        particle.updateBest(testF)
        self.assertEqual(particle.best[0], 2)
        self.assertEqual(particle.best[1], 2)

    def test_does_not_update_best_when_current_location_is_worse(self):
        particle = Particle(np.array([2, 2]), np.array([1, 1]))
        particle.best = np.array([1, 1])
        particle.updateBest(testF)
        self.assertEqual(particle.best[0], 1)
        self.assertEqual(particle.best[1], 1)

class TestParticleSwarmOptimization(unittest.TestCase):
    def test_returns_location_close_to_global_min_for_banana(self):
        bananaGlobalMin = [1,1]
        def banana(position, a=1, b=100):
            x, y = position
            return (a - x)**2 + b * (y - x**2)**2
        
        iterations=1000
        lowerBound=-2
        upperBound=2
        swarmSize=100
        globalBest, history = particleSwarmOptimization(fitness=banana, lowerBound=lowerBound, upperBound=upperBound, swarmSize=swarmSize, maxIterations=iterations)

        self.assertAlmostEqual(bananaGlobalMin[0], globalBest[0])
        self.assertAlmostEqual(bananaGlobalMin[1], globalBest[1])