# Particle Swarm Optimizer simulator

This repository includes:

1. Particle Swarm Optimizer (PSO) for resoslving optimization problems that seek to find global minimum. This PSO implementation can optimize n-dimensional optimization problems so its not restricted to 1d or 2d problems.
2. Visualization tools for making simulation videos showing how PSO solves optimization problems with 1 or 2 dimensions.

## General

## PSO implementation

## Demonstrations

The following PSO demonstrations have constant inertia and cognitive and social coefficients. Only swarm sizes and iteration counts vary

### 1d schwefel function

A relatively small

https://github.com/user-attachments/assets/5261b322-c77c-4f34-9dd5-6cd4825a5e33

 swarm quickly converges near the optimal solution.

<video width="640" height="360"  controls autoplay loop>
  <source src="resources/1d_schwefel.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### 2d schwefel function

A small swarm has a high risk to get stuck in local minima (global minima marked by blue star):

<video width="640" height="360"  controls autoplay loop>
  <source src="resources/2d_schwefel_function_stuck.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

But larger swarm almost certainly finds the global minimum from the search space. In the following swarm begins swarming around a local minimum but then some particles doing global search start registering better solution and eventually swarm moves towards the global minimum.

<video width="640" height="360"  controls autoplay loop>
  <source src="resources/2d_schwefel_function_100_particles.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Banana function

With banana function (also known as Rosenbrock function) the swarm quickly locates the global minimum but it takes many iterations until particles stop doing global searches and swarm stabilizes around the optimal solution

https://github.com/user-attachments/assets/55229e3b-0f76-4d15-b6b3-18eb99d9d8e8

## Development

run tests:
python -m unittest discover tests
