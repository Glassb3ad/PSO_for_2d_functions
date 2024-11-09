import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def visualize3dPSOHistory(history, fitness, lowerBound, upperBound, iterations, optimalSolution=None, functionName="optimization_problem"):
    # Set up 3D figure and axis
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Generate a meshgrid for the 3D fitness function landscape
    x = np.linspace(lowerBound, upperBound, 100)
    y = np.linspace(lowerBound, upperBound, 100)
    X, Y = np.meshgrid(x, y)
    # Compute Z as a 2D array matching X and Y
    Z = np.array([[fitness(np.array([X[i, j], Y[i, j]])) for j in range(X.shape[1])] for i in range(X.shape[0])])
    
    # Plot the 3D surface of the fitness function
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.3, edgecolor='none')
    
    # Add optimal solution marker if provided
    if optimalSolution is not None:
        optimal_x, optimal_y, optimal_z = optimalSolution
        ax.scatter(optimal_x, optimal_y, optimal_z, color='blue', s=100, marker='*', label="Optimal Solution")

    ax.set_title('Particle Swarm Optimization for ' + functionName)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Fitness(X, Y)')
    
    # Initialize particle scatter plot
    scat = ax.scatter([], [], [], color='r', label="Particles")
    
    # Text objects for iteration number and swarm size
    iterationText = ax.text2D(0.05, 0.95, '', transform=ax.transAxes, fontsize=12, color='black')
    swarmSizeText = ax.text2D(0.05, 0.90, '', transform=ax.transAxes, fontsize=12, color='black')
    
    # Update function for animation
    def update(frame):
        positions = np.array(history[frame])
        x_data = positions[:, 0]
        y_data = positions[:, 1]
        z_data = np.array([fitness(np.array([x, y])) for x, y in zip(x_data, y_data)])
        
        # Update particle positions in 3D scatter
        scat._offsets3d = (x_data, y_data, z_data)
        iterationText.set_text(f'Iteration: {frame + 1}/{iterations}')
        swarmSizeText.set_text(f'Swarm Size: {len(positions)}')
        
        if frame % 10 == 0:  # Print progress every 10 frames
            print(f'Processing frame {frame + 1}/{iterations} ({(frame + 1) / iterations * 100:.2f}%)')
        
        return scat, iterationText, swarmSizeText
    
    # Create the animation
    ani = animation.FuncAnimation(fig, update, frames=iterations, interval=500, blit=False)
    
    # Save the animation as a video
    ani.save(functionName + '.mp4', writer='ffmpeg', fps=10)
    print("Animation saved")

