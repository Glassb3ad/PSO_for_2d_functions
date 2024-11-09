import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def visualize1dPSOHistory(history, fitness, lowerBound, upperBound, iterations, optimalSolution=None, functionName="optimization_problem"):
    # Visualization using matplotlib and animation
    fig, ax = plt.subplots(figsize=(8, 6))

    # Create the 1D function for plotting
    x = np.linspace(lowerBound, upperBound, 400)
    y = np.array([fitness(np.array([xi])) for xi in x])  # Correctly compute fitness for each point in x

    # Plot the fitness function
    ax.plot(x, y, label="Fitness Function", color='blue')

    # If an optimal solution is provided, plot it
    if optimalSolution is not None:
        optimal_x = optimalSolution[0]
        optimal_y = fitness(optimalSolution)

        # Plot the optimal solution marker (vertical line or point)
        ax.scatter(optimal_x, optimal_y, color='green', s=50, zorder=5, marker='x', label="Optimal Solution")

    ax.set_title('Particle Swarm Optimization for ' + functionName)
    ax.set_xlabel('x')
    ax.set_ylabel('Fitness(x)')

    # Initialize particles plot (as red dots)
    scat = ax.scatter([], [], color='r', label="Particles")

    # Text object for displaying iteration number
    iterationText = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=12, color='black')
    swarmSizeText = ax.text(0.05, 0.90, '', transform=ax.transAxes, fontsize=12, color='black')

    # Update function for animation
    def update(frame):
        positions = np.array(history[frame])  # Get the particle positions for this iteration
        fitness_values = np.array([fitness(np.array([pos])) for pos in positions])  # Get fitness values

        # Update the scatter plot with new positions (x values) and corresponding fitness values (y values)
        scat.set_offsets(np.column_stack((positions, fitness_values)))
        iterationText.set_text(f'Iteration: {frame + 1}/{iterations}')  # Update iteration text
        swarmSizeText.set_text(f'Swarm Size: {len(positions)}')  # Display the swarm size (number of particles)

        if frame % 10 == 0:  # Print progress every 10 frames (you can adjust this)
            print(f'Processing frame {frame + 1}/{iterations} ({(frame + 1) / iterations * 100:.2f}%)')

        return scat, iterationText, swarmSizeText

    # Create the animation
    ani = animation.FuncAnimation(fig, update, frames=iterations, interval=500, blit=True)

    # Save the animation as a video
    ani.save(functionName + '.mp4', writer='ffmpeg', fps=10)
    print("Animation saved")
