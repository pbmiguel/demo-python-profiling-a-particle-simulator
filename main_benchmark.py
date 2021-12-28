from random import uniform

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
