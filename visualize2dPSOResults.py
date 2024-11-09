import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def visualize2dPSOHistory(history, fitness, lowerBound, upperBound, iterations,filename="pso_optimization", ):
    #    Visualization using matplotlib and animation
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(lowerBound, upperBound, 400)
    y = np.linspace(lowerBound, upperBound, 400)
    X, Y = np.meshgrid(x, y)
    Z = fitness(np.array([X, Y]))

    # Create a contour plot of the fitness function
    contour = ax.contour(X, Y, Z, 25, cmap='viridis')
    plt.colorbar(contour)

    ax.set_title('Particle Swarm Optimization')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Initialize particles plot
    scat = ax.scatter([], [], color='r')

    # Text object for displaying iteration number
    iterationText = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=12, color='black')

    # Update function for animation
    def update(frame):
        positions = np.array(history[frame])
        scat.set_offsets(positions)  # Update particle positions
        iterationText.set_text(f'Iteration: {frame + 1}/{iterations}')

        if frame % 10 == 0:  # Print progress every 10 frames (you can adjust this)
            print(f'Processing frame {frame + 1}/{iterations} ({(frame + 1) / iterations * 100:.2f}%)')

        return scat,

    # Create the animation
    ani = animation.FuncAnimation(fig, update, frames=iterations, interval=10000, blit=True)

    # Save the animation as a video
    ani.save(filename + '.mp4', writer='ffmpeg', fps=30)
    print("animation saved")


