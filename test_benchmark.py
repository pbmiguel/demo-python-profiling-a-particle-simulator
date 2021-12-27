from random import uniform
from main import Particle, ParticleSimulator

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


if __name__ == '__main__':
    benchmark()
