# Particle Swarm Optimizer simulator

This repository includes:

1. Particle Swarm Optimizer (PSO) for resoslving optimization problems that seek to find global minimum. This PSO implementation can optimize n-dimensional optimization problems so its not restricted to 1d or 2d problems.
2. Visualization tools for making simulation videos showing how PSO solves optimization problems with 1 or 2 dimensions.

## General

## PSO implementation

## Demonstrations

The following PSO demonstrations have constant inertia and cognitive and social coefficients. Only swarm sizes and iteration counts vary

### 1d schwefel function

A relatively small swarm quickly converges near the optimal solution.
https://github.com/user-attachments/assets/035f87f2-2236-47c4-9879-5ece2c01b490

### 2d schwefel function

When searching optimal solution for 2d schwefel function, small swarm has a high risk to get stuck in local minima (global minima marked by blue star):
https://github.com/user-attachments/assets/0f38689a-576e-40b7-8201-f55a10e1e062

But larger swarm almost certainly finds the global minimum from the search space. In the following swarm begins swarming around a local minimum but then some particles doing global search start registering better solution and eventually swarm moves towards the global minimum.
https://github.com/user-attachments/assets/a996cd57-90a0-4500-8469-e0694993cc7d

### Banana function

With banana function (also known as Rosenbrock function) the swarm quickly locates the global minimum but it takes many iterations until particles stop doing global searches and swarm stabilizes around the optimal solution

https://github.com/user-attachments/assets/55229e3b-0f76-4d15-b6b3-18eb99d9d8e8

## Development

run tests:
python -m unittest discover tests
