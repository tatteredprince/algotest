Validate computational algorithms, run tests against external binary.

Set environment variable as path to the external binary and execute like this: 
```bash
$ TESTEXEC=/path/to/the/external/executable algotest/array_sorting.py
...............
----------------------------------------------------------------------
Ran 15 tests in 0.034s

OK
```
If the executable reads data from standard input set additional environment variable and execute like this:
```bash
$ TESTEXEC=/path/to/the/external/executable USESTDIN=1 algotest/array_sorting.py
...............
----------------------------------------------------------------------
Ran 15 tests in 0.034s

OK
```
Tests use Python's standard `unittest`, no additional dependencies are needed.

This repository provides tests for algorithms:
- Array sorting
- Binary search
- Digit sum
- Factorial
- Fibonacci sequence
- Monotonic sequence
- Reverse letters