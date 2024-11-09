# Particle Swarm Optimizer simulator

This repository includes:

1. Particle Swarm Optimizer (PSO) for resoslving optimization problems that seek to find global minimum. This PSO implementation can optimize n-dimensional optimization problems so its not restricted to problems with 1 or 2 dimensional search space.
2. Visualization tools for making simulation videos showing how PSO solves optimization problems with 1,2 or 3 dimensional search space.

## General

## PSO implementation

## Demonstrations

The following PSO demonstrations have constant inertia and cognitive and social coefficients. Only swarm sizes and iteration counts vary. All videos generated with tools implemented in this repository.

### 1d schwefel function

A relatively small swarm quickly converges near the optimal solution.

https://github.com/user-attachments/assets/517655ba-0ab4-4749-a2ee-b1a474cc5967


### 2d schwefel function

When searching optimal solution for 2d schwefel function, small swarm has a high risk to get stuck in local minima (global minima marked by blue star):

https://github.com/user-attachments/assets/0f38689a-576e-40b7-8201-f55a10e1e062

But larger swarm almost certainly finds the global minimum from the search space. In the following swarm begins swarming around a local minimum but then some particles doing global search start registering better solution and eventually swarm moves towards the global minimum.

https://github.com/user-attachments/assets/5c596fce-c57c-4cd6-8a93-4d8a81eda4eb

### Banana function

With banana function (also known as Rosenbrock function) the swarm quickly locates the global minimum but it takes many iterations until particles stop doing global searches and swarm stabilizes around the optimal solution

https://github.com/user-attachments/assets/55229e3b-0f76-4d15-b6b3-18eb99d9d8e8

### 3d schwefel function

PSO works well in 3d search space. At first swarm is stuck in local minimum but in the end the global minimum is found

https://github.com/user-attachments/assets/408262bb-af77-4032-b91c-90d7245ce0ee

## Development

run tests: python -m unittest discover tests

tests might take some time due to using PSO with big swarms and high iteration count.
