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
