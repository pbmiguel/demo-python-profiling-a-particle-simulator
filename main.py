from matplotlib import pyplot as plt
from matplotlib import animation


"""
"""
class Particle:
    def __init__(self, x, y, ang_speed):
        self.x = x
        self.y = y
        self.ang_speed = ang_speed


"""
we have to carry out the following steps to calculate the particle position at time t:
"""
class ParticleSimulator:
    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt / timestep)
        for i in range(nsteps):
            for p in self.particles:
                norm = (p.x ** 2 + p.y ** 2) ** 0.5
                v_x = (-p.y) / norm
                v_y = p.x / norm

                d_x = timestep * p.ang_speed * v_x
                d_y = timestep * p.ang_speed * v_y
                p.x += d_x
                p.y += d_y


"""
The visualize function takes a particle ParticleSimulator instance as an argument and displays the trajectory in an animated plot. 
The steps necessary to display the particle trajectory using the matplotlib tools are as follows:
"""
def visualize(simulator):
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]
    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')

    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        simulator.evolve(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]
        line.set_data(X, Y)
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init, blit=False)
    anim.save('animation.mp4', writer='ffmpeg', fps=30)
    plt.show()


"""
To test things out, we define a small function:
- test_visualize, that animates a system of three particles rotating in different directions. 
Note that the third particle completes a round three times faster than the others:
"""
def test_visualize():
    particles = [
        Particle(0.3, 0.5, +1),
        Particle(0.0, -0.5, -1),
        Particle(-0.1,-0.4, 3)
    ]
    simulator = ParticleSimulator(particles)
    visualize(simulator)


if __name__ == '__main__':
    test_visualize()
