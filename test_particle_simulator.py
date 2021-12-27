import unittest

from main import Particle, ParticleSimulator

"""
Our test will take three particles, simulate them for 0.1 time units, 
    and compare the results with those from a reference implementation.
Note that, in this case, we compare floating point numbers up to a 
    certain precision through the fequal function:
"""
class ParticleSimulatorTestCase(unittest.TestCase):
    def test_evolve__with_3_particles_returns_correct_positions(self):
        # arrange
        particles = [
            Particle(0.3, 0.5, +1),
            Particle(0.0, -0.5, -1),
            Particle(-0.1, -0.4, +3),
        ]

        simulator = ParticleSimulator(particles)

        # act
        simulator.evolve(0.1)

        # assert
        p0, p1, p2 = particles

        def fequal(a, b, eps=1e-5):
            return abs(a-b) < eps

        self.assertTrue(fequal(p0.x, 0.210269))
        self.assertTrue(fequal(p0.y, 0.543863))

        self.assertTrue(fequal(p1.x, -0.099334))
        self.assertTrue(fequal(p1.y, -0.490034))

        self.assertTrue(fequal(p2.x, 0.191358))
        self.assertTrue(fequal(p2.y, -0.365227))

if __name__ == '__main__':
    unittest.main()
