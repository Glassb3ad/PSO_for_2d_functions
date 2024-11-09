import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def visualize2dPSOHistory(history, fitness, lowerBound, upperBound, iterations, optimalSolution=None, functionName="optimization_problem"):
    #    Visualization using matplotlib and animation
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(lowerBound, upperBound, 400)
    y = np.linspace(lowerBound, upperBound, 400)
    X, Y = np.meshgrid(x, y)
    Z = fitness(np.array([X, Y]))

    # Create a contour plot of the fitness function
    contour = ax.contour(X, Y, Z, 25, cmap='viridis')
    plt.colorbar(contour)


    ax.set_title('Particle Swarm Optimization for ' + functionName)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Initialize particles plot
    scat = ax.scatter([], [], color='r')

    # Initialize optimal solution marker (if provided)
    if optimalSolution is not None:
        optimal_x, optimal_y = optimalSolution
        ax.scatter(optimal_x, optimal_y, color='blue', s=100, marker='*', label="Optimal Solution")

    # Text object for displaying iteration number
    iterationText = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=12, color='black')
    swarmSizeText = ax.text(0.05, 0.90, '', transform=ax.transAxes, fontsize=12, color='black')

    # Update function for animation
    def update(frame):
        positions = np.array(history[frame])
        scat.set_offsets(positions)  # Update particle positions
        iterationText.set_text(f'Iteration: {frame + 1}/{iterations}')
        swarmSizeText.set_text(f'Swarm Size: {len(positions)}')  # Display the swarm size (number of particles)

        if frame % 10 == 0:  # Print progress every 10 frames (you can adjust this)
            print(f'Processing frame {frame + 1}/{iterations} ({(frame + 1) / iterations * 100:.2f}%)')

        return scat,

    # Create the animation
    ani = animation.FuncAnimation(fig, update, frames=iterations, interval=10000, blit=True)

    # Save the animation as a video
    ani.save(functionName + '.mp4', writer='ffmpeg', fps=20)
    print("animation saved")


