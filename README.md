# Particle Swarm Optimizer simulator

This repository includes:

1. Particle Swarm Optimizer (PSO) for resoslving optimization problems that seek to find global minimum. This PSO implementation can optimize problems with n-dimensional search space so its not restricted to 1 or 2 dimensions.
2. Visualization tools for making simulation videos showing how PSO solves optimization problems with 1,2 or 3 dimensional search space.

## General

PSO is a method for solving various optimization problems. An optimization problem involves finding the best possible solution for a given task. Typically, we treat tasks as functions and define the best solution as the input that the function maps to the desired output. In this case, we seek to find the input for which the function produces the smallest output. This is referred to as the global minimum.

The set of possible solutions is called the search space, and it is often bound but not finite. For example, the search space might consist of real numbers in the range from 0 to 1. Solving the optimization task for function F is to find 𝑥 from the search space such that there is no 𝑦 in the search space for which F(x)>F(y).

PSO is a nature-inspired algorithm that mimics birds' flocking behavior. The basic idea is to create a swarm of particles that move through the search space according to simple rules, and eventually, the population organizes itself around the optimal solution. Thus, PSO is a form of self-organization. The swarm's ability to find the optimal solution can be seen as an emergent property since no individual in the swarm has this ability on its own.

Each particle in the swarm represents an input to the function. It remembers its best position, and its movement is influenced by its personal best position, the global best position (i.e., the best position any particle has visited), and by random disturbances. The use of randomness is what makes PSO a stochastic algorithm. The value or fitness of position p is F(p), where F is the objective function. The particles move for a given number of iterations, after which the global best is hopefully a good enough, if not the best, solution

## Does PSO show intelligent behavior?

There is a conception of intelligence that focuses on a system’s ability to adapt to different environments. It’s easy to interpret PSO as a method for solving specific tasks in various environments, with different environments here represented by objective functions with given ranges. PSO does not inherently contain information on how to behave in different environments. Instead, it uses methods that eventually organize the swarm around the optimal solution in a multitude of environments.

The intelligent behavior is perhaps best associated with the swarm as a whole, since the behavior of individual particles is not inherently intelligent. A single particle is unable to adapt to different environments on its own.

However, intelligence of PSO can be undermined by competing conceptions of intelligence. For example, we cannot say that swarm understands or learns the problem it is working with: swarm cannot tell what function F returns for any x. This might be in contrast with neural networks which can actually learn functions (they learn which input maps to which output). The swarm simply converges to the point where the given function returns the lowest value.

## PSO implementation

The implementation relies heavily on the Particle class, which provides all the methods for controlling a particle’s state. Another key component is the particleSwarmOptimization() function, which both updates the swarm's state and records its history to visualize how the swarm searches for a solution. All relevant code for PSO can be found in the pso.py file.

### particleSwarmOptimization()

1. initialize swarm with generateInitialSwarm()
2. calculate initial global best
3. record initial swarm state
4. While iteration limit is not reached:
   1. for each particle P in swarm:
      1. update velocity
      2. move particle in search space
      3. update personal best
   2. update global best
   3. record swarm state
5. return history and global best

The particleSwarmOptimization() function accepts inertia, cognitive, and social parameters. These are hyperparameters used in the algorithm's most central operation: the velocity update.

### Particle class

The most essential method in the Particle class is updateVelocity(), which updates the particle's velocity. The equation for calculating the new velocity is a sum of three components: inertia, cognitive, and social.

I=inertia, C=cognitive, S=social, V=current velocity, P = current position, gB=global best, pB = personal best, R1 = random vector (same shape with velocity), R2 = random vector.

1. Inertia = I \* V. Inertia part represents the weight of previous velocity.
2. congnitive = C \* R1 \* (pB - P). This part motivates particles to move towards their personal best.
3. social = S \* R2 \* (gB - P). This part motivates particles to move towards the global best.

new velocity = inertia + cognitive + social

Now we see that the idea point of inertia, cognitive and social hyperparameters is to control how much particles give weight to global best (swarms social behavior), personal best (individual preference) and inertia (current velocity). By changing these hyperparameters we can, for example, try swarms where particles have more tendency to explore areas around their personal best.

Note also that both the cognitive and social components are affected by random disturbances. Kennedy and Eberhart (pioneers in swarm intelligence) provide two reasons for introducing randomness: 1) By randomly selecting the next position within the constraints described in the velocity equation, particles are protected from potentially biased decision heuristics; and 2) randomness introduces creativity, encouraging particles to try new positions (Kennedy and Eberhart, 2001). The effect of randomness on swarm creativity is perhaps visible in the following figures, which show all positions visited by the swarm during PSO. The left side shows PSO with fixed R1 and R2, and the right side shows the familiar PSO with random factors. 

![compare_fixed_and_random_PSO](https://github.com/user-attachments/assets/a95f0816-66ee-42fe-b426-df821e199325)

PSO with random factors clearly does more exploration than the fixed PSO. This means that stochastic PSO tries out more distant alternatives which can be thought as some form of creativity.

## Demonstrations

The following PSO demonstrations use constant inertia, cognitive, and social coefficients. Only the swarm sizes and iteration counts vary. All videos were generated with tools implemented in this repository.

### 1d schwefel function

A relatively small swarm quickly converges toward the optimal solution.

https://github.com/user-attachments/assets/517655ba-0ab4-4749-a2ee-b1a474cc5967

### 2d schwefel function

When searching for the optimal solution to the 2D Schwefel function, a small swarm has a high risk of getting stuck in local minima (with the global minimum marked by a blue star):

https://github.com/user-attachments/assets/0f38689a-576e-40b7-8201-f55a10e1e062

However, a larger swarm almost certainly finds the global minimum within the search space. In the following example, the swarm initially gathers around a local minimum, but then some particles conducting a global search begin registering better solutions, and eventually, the swarm moves toward the global minimum.

https://github.com/user-attachments/assets/5c596fce-c57c-4cd6-8a93-4d8a81eda4eb

### Banana function

With the banana function (also known as the Rosenbrock function), the swarm quickly locates the global minimum, but it takes many iterations for the particles to stop conducting global searches, and for the swarm to stabilize around the optimal solution.

https://github.com/user-attachments/assets/55229e3b-0f76-4d15-b6b3-18eb99d9d8e8

### 3d schwefel function

PSO works well in a 3D search space. Initially, the swarm gets stuck in a local minimum, but eventually, the global minimum is found.

https://github.com/user-attachments/assets/c9612e9d-20d2-4c40-8c7d-fa27b81f72a2

## Development

run tests: python -m unittest discover tests

tests might take some time due to using PSO with big swarms and high iteration count.

Other dependencies:

- matPlot
- numpy

The code includes sample optimization problems in separate files like optimizeBananaFunction.py. These were used to generate visuals shown in this documentation.

## references

The PSO implementation is based on the pseudocode found in Gad 2020. Also "general" and "PSO implementation" sections of this documentation rely heavily on this paper. The visualization tools were done together with chatGPT.

Ahmed G. Gad, 2020, "Particle Swarm Optimization Algorithm and Its Applications:
A Systematic Review", Archives of Computational Methods in Engineering (2022) 29:2531–2561.

James Kennedy & Russell C. Eberhart, 2001, Swarm Intelligence, Academic Press.
