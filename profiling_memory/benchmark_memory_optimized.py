"""
Optimizing Memory Consumption Using Slots
- We can use slots on the Particle class to reduce its memory footprint.
- This feature saves some memory by avoiding storing the variables of the instance in an internal dictionary.
- This strategy, however, has a drawback--it prevents the addition of attributes other than the ones specified in slots
"""
from random import uniform

"""
A test ensures the correctness of our functionality but 
    gives little information about its running time.
"""
def benchmark_memory():
    particles = [
        Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)) for _ in range(100000)
    ]

    simulator = ParticleSimulator(particles)
    simulator.evolve(0.001)

"""
Ignore: Simulator Code
"""

"""
Memory Optimization Technique Using __slots__
We can use slots on the Particle class to reduce its memory footprint. 
This feature saves some memory by avoiding storing the variables of the instance in an internal dictionary. 
"""
class Particle:
    __slots__ = ('x', 'y', 'ang_speed')

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

    def evolve_old(self, dt):
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

    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt / timestep)
        for p in self.particles:
            t_x_ang = timestep * p.ang_speed
            for i in range(nsteps):
                norm = (p.x**2 + p.y**2)**0.5
                p.x, p.y = (p.x - t_x_ang * p.y/norm,
                            p.y + t_x_ang * p.x/norm)

"""
A test ensures the correctness of our functionality but 
    gives little information about its running time.
"""
def benchmark():
    particles = [
        # What is the uniform method?
        # gives you a random floating point number in the range [a, b],
        #   (where rounding may end up giving you b).
        # ref: https://stackoverflow.com/questions/30030659/in-python-what-is-the-difference-between-random-uniform-and-random-random/53817495
        Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)) for _ in range(1000)
    ]

    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)
