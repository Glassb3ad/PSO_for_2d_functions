import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def visualize3dPSOHistory(history, fitness, lowerBound, upperBound, iterations, optimalSolution=None, functionName="optimization_problem"):
    # Set up 3D figure and axis
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Set axis limits based on search space bounds
    ax.set_xlim(lowerBound, upperBound)
    ax.set_ylim(lowerBound, upperBound)
    ax.set_zlim(lowerBound, upperBound)
    
    # Generate slices in the 3D color field
    slice_positions = np.linspace(lowerBound, upperBound, 25)  # 10 slices across the z-dimension
    x = np.linspace(lowerBound, upperBound, 100)
    y = np.linspace(lowerBound, upperBound, 100)
    X, Y = np.meshgrid(x, y)
    
    for z in slice_positions:
        Z = np.full_like(X, z)
        # Calculate the fitness value for each (x, y, z) in this slice
        fitness_values = np.array([fitness(np.array([x_val, y_val, z])) for x_val, y_val in zip(X.ravel(), Y.ravel())])
        fitness_values = fitness_values.reshape(X.shape)
        fitness_normalized = (fitness_values - fitness_values.min()) / (fitness_values.max() - fitness_values.min())
        
        # Plot this slice as a surface with transparency
        ax.plot_surface(X, Y, Z, facecolors=plt.cm.viridis(fitness_normalized), alpha=0.1, rstride=5, cstride=5, edgecolor='none')

    # Add optimal solution marker if provided
    if optimalSolution is not None:
        optimal_x, optimal_y, optimal_z = optimalSolution
        ax.scatter(optimal_x, optimal_y, optimal_z, color='blue', s=100, marker='*', label="Optimal Solution")

    ax.set_title('Particle Swarm Optimization for ' + functionName)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # Initialize particle scatter plot
    scat = ax.scatter([], [], [], color='r', s=30, label="Particles")

    # Text objects for iteration number and swarm size
    iterationText = ax.text2D(0.05, 0.95, '', transform=ax.transAxes, fontsize=12, color='black')
    swarmSizeText = ax.text2D(0.05, 0.90, '', transform=ax.transAxes, fontsize=12, color='black')
    
    # Update function for animation
    def update(frame):
        positions = np.array(history[frame])
        x_data = positions[:, 0]
        y_data = positions[:, 1]
        z_data = positions[:, 2]
        
        # Update particle positions
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
