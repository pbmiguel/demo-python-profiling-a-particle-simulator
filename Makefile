run_benchmark_option_1:
# A very simple way to time a benchmark is through the Unix "time" command.
# Using the time command, as follows, you can easily measure the execution time of an arbitrary process:
# only on unix
	time python test_benchmark.py

### another benchmark options is to -> run timeit in IPython
## poetry run ipython
## from main_optimized import benchmark
## %timeit benchmark()

run_benchmark_option_2:
	python -m timeit -s 'from test_benchmark import benchmark' 'benchmark()'

run_benchmark_option_3:
	# run pytest-benchmark
	pytest test_particle_simulator_with_bench.py::test_evolve__with_3_particles_returns_correct_positions

profile_line_by_line:
	# poetry run ipython
	# %load_ext line_profiler
	# from main_benchmark import benchmark, ParticleSimulator
	# %lprun -f ParticleSimulator.evolve benchmark()