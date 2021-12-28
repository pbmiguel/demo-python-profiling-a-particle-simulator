# Profiling Python bytecode using the dis module

by running the `profiling_main.py` you will get the bytecode instructions per line of the evolve method

```
evolve_old has 146 byte code instructions 

20           0 LOAD_CONST               1 (1e-05)
              2 STORE_FAST               2 (timestep)

 21           4 LOAD_GLOBAL              0 (int)
              6 LOAD_FAST                1 (dt)
              8 LOAD_FAST                2 (timestep)
             10 BINARY_TRUE_DIVIDE
             12 CALL_FUNCTION            1
             14 STORE_FAST               3 (nsteps)

 22          16 LOAD_GLOBAL              1 (range)
             18 LOAD_FAST                3 (nsteps)
             20 CALL_FUNCTION            1
             22 GET_ITER
        >>   24 FOR_ITER               118 (to 144)
             26 STORE_FAST               4 (i)

 23          28 LOAD_FAST                0 (self)
             30 LOAD_ATTR                2 (particles)
             32 GET_ITER
        >>   34 FOR_ITER               106 (to 142)
             36 STORE_FAST               5 (p)

 24          38 LOAD_FAST                5 (p)
             40 LOAD_ATTR                3 (x)
             42 LOAD_CONST               2 (2)
             44 BINARY_POWER
             46 LOAD_FAST                5 (p)
             48 LOAD_ATTR                4 (y)
             50 LOAD_CONST               2 (2)
             52 BINARY_POWER
             54 BINARY_ADD
             56 LOAD_CONST               3 (0.5)
             58 BINARY_POWER
             60 STORE_FAST               6 (norm)

 25          62 LOAD_FAST                5 (p)
             64 LOAD_ATTR                4 (y)
             66 UNARY_NEGATIVE
             68 LOAD_FAST                6 (norm)
             70 BINARY_TRUE_DIVIDE
             72 STORE_FAST               7 (v_x)

 26          74 LOAD_FAST                5 (p)
             76 LOAD_ATTR                3 (x)
             78 LOAD_FAST                6 (norm)
             80 BINARY_TRUE_DIVIDE
             82 STORE_FAST               8 (v_y)

 28          84 LOAD_FAST                2 (timestep)
             86 LOAD_FAST                5 (p)
             88 LOAD_ATTR                5 (ang_speed)
             90 BINARY_MULTIPLY
             92 LOAD_FAST                7 (v_x)
             94 BINARY_MULTIPLY
             96 STORE_FAST               9 (d_x)

 29          98 LOAD_FAST                2 (timestep)
            100 LOAD_FAST                5 (p)
            102 LOAD_ATTR                5 (ang_speed)
            104 BINARY_MULTIPLY
            106 LOAD_FAST                8 (v_y)
            108 BINARY_MULTIPLY
            110 STORE_FAST              10 (d_y)

 30         112 LOAD_FAST                5 (p)
            114 DUP_TOP
            116 LOAD_ATTR                3 (x)
            118 LOAD_FAST                9 (d_x)
            120 INPLACE_ADD
            122 ROT_TWO
            124 STORE_ATTR               3 (x)

 31         126 LOAD_FAST                5 (p)
            128 DUP_TOP
            130 LOAD_ATTR                4 (y)
            132 LOAD_FAST               10 (d_y)
            134 INPLACE_ADD
            136 ROT_TWO
            138 STORE_ATTR               4 (y)
            140 JUMP_ABSOLUTE           34
        >>  142 JUMP_ABSOLUTE           24
        >>  144 LOAD_CONST               0 (None)
            146 RETURN_VALUE

evolve_new has 124 bytecode instructions
 34           0 LOAD_CONST               1 (1e-05)
              2 STORE_FAST               2 (timestep)

 35           4 LOAD_GLOBAL              0 (int)
              6 LOAD_FAST                1 (dt)
              8 LOAD_FAST                2 (timestep)
             10 BINARY_TRUE_DIVIDE
             12 CALL_FUNCTION            1
             14 STORE_FAST               3 (nsteps)

 36          16 LOAD_FAST                0 (self)
             18 LOAD_ATTR                1 (particles)
             20 GET_ITER
        >>   22 FOR_ITER                98 (to 122)
             24 STORE_FAST               4 (p)

 37          26 LOAD_FAST                2 (timestep)
             28 LOAD_FAST                4 (p)
             30 LOAD_ATTR                2 (ang_speed)
             32 BINARY_MULTIPLY
             34 STORE_FAST               5 (t_x_ang)

 38          36 LOAD_GLOBAL              3 (range)
             38 LOAD_FAST                3 (nsteps)
             40 CALL_FUNCTION            1
             42 GET_ITER
        >>   44 FOR_ITER                74 (to 120)
             46 STORE_FAST               6 (i)

 39          48 LOAD_FAST                4 (p)
             50 LOAD_ATTR                4 (x)
             52 LOAD_CONST               2 (2)
             54 BINARY_POWER
             56 LOAD_FAST                4 (p)
             58 LOAD_ATTR                5 (y)
             60 LOAD_CONST               2 (2)
             62 BINARY_POWER
             64 BINARY_ADD
             66 LOAD_CONST               3 (0.5)
             68 BINARY_POWER
             70 STORE_FAST               7 (norm)

 40          72 LOAD_FAST                4 (p)
             74 LOAD_ATTR                4 (x)
             76 LOAD_FAST                5 (t_x_ang)
             78 LOAD_FAST                4 (p)
             80 LOAD_ATTR                5 (y)
             82 BINARY_MULTIPLY
             84 LOAD_FAST                7 (norm)
             86 BINARY_TRUE_DIVIDE
             88 BINARY_SUBTRACT

 41          90 LOAD_FAST                4 (p)
             92 LOAD_ATTR                5 (y)
             94 LOAD_FAST                5 (t_x_ang)
             96 LOAD_FAST                4 (p)
             98 LOAD_ATTR                4 (x)
            100 BINARY_MULTIPLY
            102 LOAD_FAST                7 (norm)
            104 BINARY_TRUE_DIVIDE
            106 BINARY_ADD

 40         108 ROT_TWO
            110 LOAD_FAST                4 (p)
            112 STORE_ATTR               4 (x)
            114 LOAD_FAST                4 (p)
            116 STORE_ATTR               5 (y)
            118 JUMP_ABSOLUTE           44
        >>  120 JUMP_ABSOLUTE           22
        >>  122 LOAD_CONST               0 (None)
            124 RETURN_VALUE
```

LOAD_FAST loads a reference of the p variable onto the stack
LOAD_ATTR loads the y attribute of the item present on top of the stack.
The other instructions, UNARY_NEGATIVE and BINARY_TRUE_DIVIDE, simply do arithmetic operations on top-of-stack items
Finally, the result is stored in v_x (STORE_FAST)

1. You should be able to compare the number of bytecode instructions of the old vs new evolve method
2. Goal is reduce the amount of instructions
Note that this approach is ultimately limited by the speed of the Python interpreter and it is probably not the right tool for the job.