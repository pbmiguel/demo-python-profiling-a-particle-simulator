# Profiling Memory with memory_profiler

We can benchmark using IPython
1. poetry run ipython
2. %load_ext memory_profiler
3. from profiling_memory.benchmark_memory import benchmark_memory
4. %mprun -f benchmark_memory benchmark_memory()

which will return
```
WARNING: the memory profiler has very volatile results (sometimes with a difference ~30MiB)

old evolve method consumes at most 72Mib (Mib != MB)
But From the Increment column, we can see that 100,000 Particle objects take 15.7 MiB of memory

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     45.9 MiB     45.9 MiB           1   def benchmark_memory():
     8     71.8 MiB     10.0 MiB      100004       particles = [
     9     71.8 MiB     15.9 MiB      100001           Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)) for _ in range(100000)
    10                                             ]
    11                                         
    12     71.8 MiB      0.0 MiB           1       simulator = ParticleSimulator(particles)
    13     71.8 MiB      0.0 MiB           1       simulator.evolve_old(0.001)


new evolve method consumes at most 95Mib
But From the Increment column, we can see that 100,000 Particle objects take 12 MiB of memory

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     75.4 MiB     75.4 MiB           1   def benchmark_memory():
     8     94.6 MiB      7.7 MiB      100004       particles = [
     9     94.6 MiB     11.6 MiB      100001           Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)) for _ in range(100000)
    10                                             ]
    11                                         
    12     94.6 MiB      0.0 MiB           1       simulator = ParticleSimulator(particles)
    13     94.6 MiB      0.0 MiB           1       simulator.evolve(0.001)

```

# Optimizing Memory Consumption Using Slots
to reduce memory footprint use slots in the `Particles`
- run the `benchmark_memory_optimized`
- By rewriting the Particle class using __slots__, we can save about 10 MiB of memory

```
notice the 10Mib reduction in Mem usage

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    13     64.6 MiB     64.6 MiB           1   def benchmark_memory():
    14     79.5 MiB      8.9 MiB      100004       particles = [
    15     79.5 MiB      6.0 MiB      100001           Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)) for _ in range(100000)
    16                                             ]
    17                                         
    18     79.5 MiB      0.0 MiB           1       simulator = ParticleSimulator(particles)
    19     79.5 MiB      0.0 MiB           1       simulator.evolve(0.001)

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     65.3 MiB     65.3 MiB           1   def benchmark_memory():
     8     88.9 MiB     10.6 MiB      100004       particles = [
     9     88.9 MiB     12.9 MiB      100001           Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)) for _ in range(100000)
    10                                             ]
    11                                         
    12     88.9 MiB      0.0 MiB           1       simulator = ParticleSimulator(particles)
    13     88.9 MiB      0.0 MiB           1       simulator.evolve(0.001)


```