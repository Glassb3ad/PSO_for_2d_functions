import matplotlib.pyplot as plt
import numpy as np

def visualize2dPSOVisited(history, fitness, lowerBound, upperBound, optimalSolution=None, functionName="optimization_problem"):
    # Visualization using matplotlib (static image)
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(lowerBound, upperBound, 400)
    y = np.linspace(lowerBound, upperBound, 400)
    X, Y = np.meshgrid(x, y)
    Z = fitness(np.array([X, Y]))

    # Create a contour plot of the fitness function
    contour = ax.contour(X, Y, Z, 25, cmap='viridis')
    plt.colorbar(contour)

    ax.set_title('Particle Swarm Optimization History for ' + functionName)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Plot all particle positions from history
    for frame_positions in history:
        positions = np.array(frame_positions)
        ax.scatter(positions[:, 0], positions[:, 1], color='red', alpha=0.3, s=10)

    # Mark the optimal solution if provided
    if optimalSolution is not None:
        optimal_x, optimal_y = optimalSolution
        ax.scatter(optimal_x, optimal_y, color='blue', s=100, marker='*', label="Optimal Solution")

    plt.legend()
    plt.savefig(functionName, dpi=300)
    print(f"Image saved at {functionName}")
