run_benchmark_option_1:
# A very simple way to time a benchmark is through the Unix "time" command.
# Using the time command, as follows, you can easily measure the execution time of an arbitrary process:
# only on unix
	time python test_benchmark.py

run_benchmark_option_2:
	python -m timeit -s 'from test_benchmark import benchmark' 'benchmark()'
