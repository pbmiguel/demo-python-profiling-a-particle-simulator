from main import Particle, ParticleSimulator

"""
Our test will take three particles, simulate them for 0.1 time units, 
    and compare the results with those from a reference implementation.
Note that, in this case, we compare floating point numbers up to a 
    certain precision through the fequal function:
"""
def test_evolve__with_3_particles_returns_correct_positions(benchmark):
    # arrange
    particles = [
        Particle(0.3, 0.5, +1),
        Particle(0.0, -0.5, -1),
        Particle(-0.1, -0.4, +3),
    ]

    simulator = ParticleSimulator(particles)

    # act
    benchmark(simulator.evolve, 0.1)